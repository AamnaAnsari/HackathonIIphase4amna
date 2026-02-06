# MCP Tools

Define the MCP tools the agents will use (stateless wrappers around DB operations):

- `create_task(user_id, title, description)` — create a new task
- `list_tasks(user_id, filter)` — return tasks for the user
- `update_task(task_id, changes)` — apply updates to a task
- `delete_task(task_id)` — remove a task
- `create_conversation(user_id)` — start a conversation record
- `append_message(conversation_id, role, content)` — persist messages

Each tool should validate inputs, return structured outputs, and log actions to the DB.