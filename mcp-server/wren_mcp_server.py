#!/usr/bin/env python3
"""Wren CX mock MCP server — ticket inbox + CRM. Standard library only, no installs.

Speaks MCP over stdio (newline-delimited JSON-RPC 2.0). Reads sample_data/wren_tickets.json and
sample_data/crm_orders.json; writes ticket updates to mcp-server/state/tickets_state.json so the
agent's actions persist between calls (delete that file to reset the inbox).

Register in Antigravity / Claude / any MCP client as:
    command: python3
    args:    ["<path>/mcp-server/wren_mcp_server.py"]
"""
import json
import sys
import pathlib
from datetime import datetime, timezone, timedelta

ROOT = pathlib.Path(__file__).resolve().parent
DATA = ROOT.parent / "sample_data"
STATE = ROOT / "state" / "tickets_state.json"
IST = timezone(timedelta(hours=5, minutes=30))

VALID_STATUS = {"pending", "auto_resolved", "awaiting_customer", "escalated", "human_review", "rejected"}
VALID_CLASS = {"ORDER_ISSUE", "PRODUCT_QUERY", "RETURNS", "COMPLAINT", "BILLING", "UNKNOWN"}


def load_tickets():
    if STATE.exists():
        return json.loads(STATE.read_text(encoding="utf-8"))
    return json.loads((DATA / "wren_tickets.json").read_text(encoding="utf-8"))


def save_tickets(tickets):
    STATE.parent.mkdir(exist_ok=True)
    STATE.write_text(json.dumps(tickets, indent=2, ensure_ascii=False), encoding="utf-8")


CRM = json.loads((DATA / "crm_orders.json").read_text(encoding="utf-8"))

TOOLS = [
    {
        "name": "get_pending_tickets",
        "description": "Read unprocessed tickets from the Wren CX support inbox (oldest first).",
        "inputSchema": {"type": "object", "properties": {
            "limit": {"type": "integer", "description": "Max tickets to return (default 5)"}}},
    },
    {
        "name": "get_order_status",
        "description": "Look up an order in the CRM. Returns status, carrier, ETA. "
                       "customer_id must own the order, otherwise access is denied.",
        "inputSchema": {"type": "object", "required": ["order_id", "customer_id"], "properties": {
            "order_id": {"type": "string", "description": "e.g. WR-84221"},
            "customer_id": {"type": "string", "description": "e.g. CUST-4821"}}},
    },
    {
        "name": "get_customer_history",
        "description": "Customer tier, AI-processing consent flag, count of tickets open > 72 hours, and the customer's order IDs.",
        "inputSchema": {"type": "object", "required": ["customer_id"], "properties": {
            "customer_id": {"type": "string"}}},
    },
    {
        "name": "update_ticket_status",
        "description": "Write the agent's decision back to the ticket system.",
        "inputSchema": {"type": "object", "required": ["ticket_id", "status", "classification"], "properties": {
            "ticket_id": {"type": "string"},
            "status": {"type": "string", "enum": sorted(VALID_STATUS)},
            "classification": {"type": "string", "enum": sorted(VALID_CLASS)},
            "note": {"type": "string", "description": "One-line reasoning, kept for audit"}}},
    },
]


def tool_get_pending_tickets(args):
    limit = int(args.get("limit", 5))
    pending = [t for t in load_tickets() if t["status"] == "pending"]
    return {"count_pending": len(pending), "tickets": pending[:limit]}


def tool_get_order_status(args):
    order = CRM["orders"].get(args["order_id"])
    if order is None:
        raise ToolError(f"Order {args['order_id']} not found")
    if order["customer_id"] != args["customer_id"]:
        # The PM's spec decision made concrete: never leak another customer's order
        raise ToolError("Access denied: order does not belong to this customer")
    return {"order_id": args["order_id"], **{k: v for k, v in order.items() if k != "customer_id"}}


def tool_get_customer_history(args):
    cust = CRM["customers"].get(args["customer_id"])
    if cust is None:
        raise ToolError(f"Customer {args['customer_id']} not found")
    order_ids = [oid for oid, o in CRM["orders"].items() if o["customer_id"] == args["customer_id"]]
    # Name withheld on purpose — data minimisation (DPDP)
    return {"customer_id": args["customer_id"], **{k: v for k, v in cust.items() if k != "name"}, "order_ids": order_ids}


def tool_update_ticket_status(args):
    if args["status"] not in VALID_STATUS:
        raise ToolError(f"Invalid status. Use one of: {sorted(VALID_STATUS)}")
    if args["classification"] not in VALID_CLASS:
        raise ToolError(f"Invalid classification. Use one of: {sorted(VALID_CLASS)}")
    tickets = load_tickets()
    for t in tickets:
        if t["ticket_id"] == args["ticket_id"]:
            t.update(status=args["status"], classification=args["classification"],
                     note=args.get("note", ""), updated_at=datetime.now(IST).isoformat(timespec="seconds"))
            save_tickets(tickets)
            return {"ok": True, "ticket_id": t["ticket_id"], "status": t["status"]}
    raise ToolError(f"Ticket {args['ticket_id']} not found")


HANDLERS = {
    "get_pending_tickets": tool_get_pending_tickets,
    "get_order_status": tool_get_order_status,
    "get_customer_history": tool_get_customer_history,
    "update_ticket_status": tool_update_ticket_status,
}


class ToolError(Exception):
    pass


def handle(msg):
    method, mid = msg.get("method"), msg.get("id")
    if mid is None:  # notification (e.g. notifications/initialized) — no reply
        return None
    if method == "initialize":
        return {"jsonrpc": "2.0", "id": mid, "result": {
            "protocolVersion": msg.get("params", {}).get("protocolVersion", "2025-06-18"),
            "capabilities": {"tools": {}},
            "serverInfo": {"name": "wren-cx-mock", "version": "1.0.0"}}}
    if method == "ping":
        return {"jsonrpc": "2.0", "id": mid, "result": {}}
    if method == "tools/list":
        return {"jsonrpc": "2.0", "id": mid, "result": {"tools": TOOLS}}
    if method == "tools/call":
        params = msg.get("params", {})
        name, args = params.get("name"), params.get("arguments") or {}
        if name not in HANDLERS:
            return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32602, "message": f"Unknown tool: {name}"}}
        try:
            out, is_error = HANDLERS[name](args), False
        except (ToolError, KeyError) as e:
            out, is_error = {"error": str(e) if isinstance(e, ToolError) else f"Missing argument: {e}"}, True
        return {"jsonrpc": "2.0", "id": mid, "result": {
            "content": [{"type": "text", "text": json.dumps(out, ensure_ascii=False)}], "isError": is_error}}
    return {"jsonrpc": "2.0", "id": mid, "error": {"code": -32601, "message": f"Method not found: {method}"}}


def main():
    # Windows defaults to a non-UTF-8 code page; the data has ₹ and the protocol is UTF-8
    sys.stdin.reconfigure(encoding="utf-8")
    sys.stdout.reconfigure(encoding="utf-8")
    if "--check" in sys.argv:  # setup check for students: data loads, then exit
        print(f"OK: Python {sys.version.split()[0]}, {len(load_tickets())} tickets, "
              f"{len(CRM['orders'])} orders. The Wren MCP server is ready.")
        return
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            reply = handle(json.loads(line))
        except json.JSONDecodeError:
            reply = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}}
        if reply is not None:
            sys.stdout.write(json.dumps(reply, ensure_ascii=False) + "\n")
            sys.stdout.flush()


if __name__ == "__main__":
    main()
