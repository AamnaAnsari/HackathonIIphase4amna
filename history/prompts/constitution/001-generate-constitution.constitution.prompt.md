---
id: 001
title: Generate Constitution
stage: constitution
date: 2025-1-26
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: unknown
command: /sp.constitution Generate a constitution.md file in my history/prompts folder for my Python CLI Todo App project. The rules must be: Stack: Use Python 3.13+ and uv for dependency management. Structure: All source code must reside in the /src folder with a modular structure. Quality: Enforce strict type hints, clean code principles, and PEP 8 standards. Storage: Data must be strictly in-memory (no external databases or files for now). Agentic Workflow: Claude must always update CLAUDE.md after changes and follow spec-driven development. Interface: The app must be a user-friendly Command Line Interface (CLI). Keep the rules concise and actionable for an AI agent.
labels: ["constitution", "project-setup"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:

---

## Prompt

Generate a constitution.md file in my history/prompts folder for my Python CLI Todo App project. The rules must be:

Stack: Use Python 3.13+ and uv for dependency management.

Structure: All source code must reside in the /src folder with a modular structure.

Quality: Enforce strict type hints, clean code principles, and PEP 8 standards.

Storage: Data must be strictly in-memory (no external databases or files for now).

Agentic Workflow: Claude must always update CLAUDE.md after changes and follow spec-driven development.

Interface: The app must be a user-friendly Command Line Interface (CLI).

Keep the rules concise and actionable for an AI agent.


## Response snapshot

Successfully generated the project constitution at .specify/memory/constitution.md with version 1.0.0. The constitution defines core principles for stack, code structure, quality, data storage, agentic workflow, and user interface for the Python CLI Todo App project. Manual follow-up is suggested for .specify/templates/plan-template.md to align its "Constitution Check" section with the new principles.

🛠️ 2. TECHNOLOGY CONSTRAINTS

- **Backend:** FastAPI (Python 3.11+) with uv
- **Frontend:** Next.js 14+ with pnpm and Shadcn/UI
- **Intelligence:** Google Gemini (via AI Agents SDK)
- **Database:** Neon PostgreSQL (Serverless)
- **Message Broker:** Redpanda Cloud (Kafka)
- **Deployment:** Kubernetes (Minikube for Dev / AKS or GKE for Prod)
- **Containerization:** Docker (Multi-stage builds)

📂 3. PROJECT STRUCTURE & SEPARATION

Microservices must be strictly decoupled:

- `src/backend`: Manages Chat-API and Task CRUD operations.
- `src/notification-service`: Consumes Kafka topics to trigger and send reminders.
- `src/frontend`: Handles the user interface and Better Auth client-side logic.
- `k8s/`: Contains all Kubernetes manifests (Deployments, Services, ConfigMaps).
- `dapr/components/`: Infrastructure configuration files (pubsub.yaml, statestore.yaml).

🧪 4. COMPLIANCE & GOVERNANCE

### I. Spec-First Development

No code implementation shall commence without the generation and approval of `/sp.specify` and `/sp.plan` documents. The AI Agent is required to generate design documentation first.

### II. Secret Management

`.env` files must never be included in Docker images or the Git repository.

Kubernetes Secrets or the Dapr Secrets API must be used for all cloud deployments.

### III. Definition of Done (DoD)

A task is considered complete only when:

- Docker images build successfully without errors.
- Events are verified on the Redpanda topic.
- Dapr sidecars are active between microservices.
- The end-to-end flow is functional on the cloud deployment (Hugging Face/GKE).

## Outcome

- ✅ Impact: Constitution created successfully.
- 🧪 Tests: No specific tests for this task.
- 📁 Files: Created .specify/memory/constitution.md
- 🔁 Next prompts: Next step is to implement based on the constitution and further spec/plan.
- 🧠 Reflection: Successfully used agent-native tools to create PHR after script failure.

## Evaluation notes (flywheel)

- Failure modes observed: Shell script `create-phr.sh` not found.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Investigate if create-phr.sh is intended to be generated or if its path is incorrect.
