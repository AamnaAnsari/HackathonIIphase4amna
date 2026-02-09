---
id: 001
title: constitution
stage: planning
date: 2026-1-26
surface: agent
model: claude-sonnet-4-5-20250929
feature: todo-core
branch: master
command: /sp.plan Generate a plan.md file based on specs/todo-spec.md and constitution.md.
labels: ["planning", "todo-app"]
links:
  constitution: ".specify/memory/constitution.md"
---

# Phase 5 Constitution: Advanced Cloud & Event-Driven Architecture

**Version:** 2.1.0

**Project:** AI-Powered Conversational Todo System

**Framework:** Spec-Kit Plus Agentic Workflow

🏛️ 1. ARCHITECTURAL MANDATES

I. Event-Driven Messaging (Redpanda/Kafka)

Communication between the system's microservices must always be asynchronous.

Principle: The Backend must always publish "Domain Events" whenever a task is created, updated, or deleted.

Infrastructure: Redpanda Cloud (Kafka API) shall be utilized as the primary message broker.

Constraint: Direct HTTP calls between microservices are strictly prohibited to ensure loose coupling.

II. Dapr Abstraction Layer

To remain infrastructure-agnostic, the system will follow the Dapr (Distributed Application Runtime) sidecar pattern.

Pub/Sub: Dapr Pub/Sub components must be used for all messaging requirements.

State Store: Dapr State Store (Redis/Postgres) shall be used for temporary data and distributed locking.

Statelessness: Backend services must be 100% stateless to enable horizontal scaling within the Kubernetes environment.

III. AI Agent Sovereignty (Gemini & MCP)

The Google Gemini LLM shall serve as the primary controller for the chat interface.

Tool-Driven: The AI must not interact with the database directly; it must perform all operations through MCP (Model Context Protocol) tools.

Context Awareness: Chat history must be persisted in Neon PostgreSQL to maintain long-term memory and context.

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

Ratified Date: February 01, 2026
