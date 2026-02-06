# [Phase 3 Ai todo chatbot] Constitution

```markdown
id	title	stage	date	surface	model	feature	branch	user	command	labels	links	files	tests
2
Phase-3 AI CUI constitution update
constitution
2025-12-19
agent
claude-opus-4-5-20251101
none
main
unknown
/sp.constitution
constitution
amendment
phase-3
ai-agents
mcp
cui
spec	ticket	adr	pr
.specify/memory/constitution.md
None (documentation only)


Prompt:
We are starting Phase 3: AI Chatbot. I need to update the Database Schema to store chat history.

Please update `backend/models.py` to add two new models strictly following the Phase 3 specs:

1.  **Conversation Model:**
    - `id`: int, primary key.
    - `user_id`: str (foreign key to users, or just indexed string if FK is disabled).
    - `created_at`: datetime (default now).
    - `updated_at`: datetime (default now).

2.  **Message Model:**
    - `id`: int, primary key.
    - `conversation_id`: int (foreign key to conversation.id).
    - `role`: str (e.g., "user" or "assistant").
    - `content`: str (The actual text).
    - `created_at`: datetime (default now).

3.  **Update `reset_db.py`:**
    - Ensure these new tables are included in the reset script so we can generate them cleanly if needed.

Refuse to delete the existing `Task` or `User` models. Just ADD the new ones.


Response snapshot
Successfully amended the project constitution from v1.0.0 to v1.1.0 (MINOR version bump).

New Principles Added (Phase-3):

VIII. Stateless Server Architecture: No in-memory state; all session and AI agent state persisted in PostgreSQL; enables horizontal scaling
IX. Tool-Driven AI Behavior (MCP): AI agents MUST use MCP tools for all operations; prevents prompt injection; provides auditable AI actions
X. Conversation Persistence: All messages stored in database; multi-turn context preserved; tool calls logged for debugging
Updated Architectural Constraints:

Added OpenAI ChatKit UI to frontend stack
Added OpenAI Agents SDK to backend stack
Added Official MCP SDK to backend stack
Added 3 new constraint validations for AI/MCP components
Preserved Principles (I-VII): All original Phase-2 principles retained without modification, ensuring backward compatibility with existing implementation.

Outcome
✅ Impact: Constitution extended with 3 new AI/CUI-specific principles, enabling Phase-3 development while preserving all Phase-2 governance
🧪 Tests: None (governance document)
📁 Files: Updated .specify/memory/constitution.md (v1.0.0 → v1.1.0, 256 lines)
🔁 Next prompts: Ready for /sp.specify to create Phase-3 CUI feature specification
🧠 Reflection: MINOR version bump appropriate as new principles ADD to existing governance without changing existing principle semantics; stateless architecture principle critical for production scalability
Evaluation notes (flywheel)
Failure modes observed: None
Graders run and results (PASS/FAIL): Not applicable (documentation amendment)
Prompt variant (if applicable): Standard constitution amendment via /sp.constitution with Phase-3 scope
Next experiment (smallest change to try): Validate new MCP/AI principles against upcoming Phase-3 spec to ensure sufficient coverage for AI agent safety and controllability
