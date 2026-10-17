# Wren CX Mock MCP Server

A stand-in for Wren's ticket inbox and CRM, so the Session 2 MCP build acts on a real (simulated) system. **Python 3 standard library only — nothing to install.**

## Tools it exposes

| Tool | What it does |
|---|---|
| `get_pending_tickets(limit)` | Reads unprocessed tickets from `sample_data/wren_tickets.json` |
| `get_order_status(order_id, customer_id)` | CRM lookup. **Refuses** if the order doesn't belong to that customer |
| `get_customer_history(customer_id)` | Tier, AI-processing consent flag, tickets open > 72h, order IDs (name withheld — data minimisation) |
| `update_ticket_status(ticket_id, status, classification, note)` | Writes the agent's decision back. Status: `pending · auto_resolved · awaiting_customer · escalated · human_review · rejected` |

Updates persist in `mcp-server/state/tickets_state.json`. **Delete that file to reset the inbox.**

## Connect it

You need `python3` on your PATH (`python3 --version`). Replace `<FULL_PATH>` with where you cloned the course folder.

**Antigravity:** Agent panel → `…` menu → **MCP Servers** → **Manage MCP Servers** → **View raw config**, and add:

```json
{
  "mcpServers": {
    "wren": {
      "command": "python3",
      "args": ["<FULL_PATH>/mcp-server/wren_mcp_server.py"]
    }
  }
}
```

**Claude Code:** `claude mcp add wren -- python3 <FULL_PATH>/mcp-server/wren_mcp_server.py`

**Claude Desktop / Cursor / VS Code:** same `mcpServers` block in that client's MCP config file.

## Check it works

Ask the agent: *"List the tools on the wren MCP server, then get 1 pending ticket."* You should see TKT-A (order WR-84221).

## If MCP won't connect (fallback)

Don't lose the session to setup. Use the **simulated tool output** in the Session 2 handbook — paste the JSON responses in by hand. The design questions (which tools, in what order, with what permissions) are the same.

## Tested

Verified 3 Oct 2026 with a live MCP client (Claude Code, `--mcp-config`): initialize → tools/list → `get_pending_tickets` → `get_order_status` → `update_ticket_status` all succeeded. Antigravity menu path to be re-checked by the instructor before 17 Oct.
