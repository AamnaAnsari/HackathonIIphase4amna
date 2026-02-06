# Agent Workflow

Outline of the AI agent workflow for Phase-3 Todo CUI:

- Trigger: User natural-language input from ChatKit frontend
- Planner: Parse intent and decompose into tool calls
- Executor: Call MCP tools (create_task, list_tasks, update_task, delete_task)
- Persistence: Log all messages and tool calls to the database
- Response: Return assistant message and any structured outputs

Safety: All operations must be performed via MCP tools to reduce injection risk.