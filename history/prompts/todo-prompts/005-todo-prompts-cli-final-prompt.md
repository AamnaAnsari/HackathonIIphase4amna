---
id: 005
title: Implement CLI and Verification
stage: implementation
date: 2025-12-28
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-ui
branch: master
command: /sp.task Implement Phase 3 and 4 from plan.md.
labels: ["implementation", "cli", "cleanup"]
links:
  plan: "plan.md"
---

## Prompt

Finalize the project by implementing Phase 3 (CLI Interface) and Phase 4 (Verification).

**Instructions:**
1. Create `src/main.py` with a robust command-line loop.
2. Connect all menu options (Add, View, Update, Delete, Toggle) to the `TodoManager`.
3. Add basic error handling for invalid user inputs (e.g., non-existent IDs).
4. Generate a `README.md` and update `CLAUDE.md` with instructions on how to run the app using `uv`.

Ensure all code passes the quality checks mentioned in the constitution.

## Response snapshot

Successfully finalized the Todo CLI application by developing the interactive user interface in `src/main.py`. The implementation bridges the `TodoManager` logic with a robust command-line loop, featuring comprehensive error handling for user inputs. Additionally, project-level documentation (`README.md`) and agent instructions (`CLAUDE.md`) were updated to reflect the full operational state of the app.



## Outcome

- ✅ **UI/UX:** Created a persistent menu loop with 6 interactive options.
- ✅ **Integration:** Seamlessly connected the CLI front-end to the `TodoManager` CRUD backend.
- ✅ **Resilience:** Implemented `try-except` blocks to handle `ValueError` during ID selection.
- ✅ **Documentation:** Finalized `README.md` with a professional layout and `CLAUDE.md` with operational guides.
- 📁 **Files:** Created `src/main.py`, `README.md`, and updated `CLAUDE.md`.

## Evaluation notes (flywheel)

- **Successes:** The separation of concerns (SOC) between the manager and the CLI allowed for rapid UI development without touching core logic.
- **Failures/Risks:** Manual testing revealed a minor bug in the update prompt; corrected by adding blank-input checks.
- **Next experiment:** Explore the use of the `rich` library in future tasks for enhanced CLI visuals (colors/tables).

## Reflection
This task completes the initial vision of the In-Memory Todo App. By adhering to the constitution's modularity rules, the app remains highly testable and ready for future persistence upgrades (e.g., JSON or SQLite).