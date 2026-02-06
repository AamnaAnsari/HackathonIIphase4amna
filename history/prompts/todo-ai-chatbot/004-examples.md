# Conversation Examples

Example 1 — Create task

User: "Create a todo to buy groceries for $50 this weekend."
Assistant (tool-driven):
- Planner decides to call `create_task` with title "Buy groceries" and description "Budget $50, this weekend".
- Assistant confirms: "Done — created task 'Buy groceries'."

Example 2 — Update task

User: "Mark my grocery task as completed."
Assistant: Calls `list_tasks` to find task, then `update_task(task_id, {completed: true})`, then replies.

Example 3 — Multi-turn clarification

User: "Remind me to water the plants every Monday."
Assistant: Asks clarifying question if scheduling feature absent; otherwise creates task and schedules reminder via tool.