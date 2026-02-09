# TodoAI: AI-Powered Todo Chatbot - Hackathon Phases Overview

Welcome to the **Todo web app Hackathon Project** — an evolution of a simple in-memory console app into a cloud-native, event-driven microservices system powered by AI.

## 📋 Hackathon Phases

| Phase | Description | Technology Stack | Points | Due Date |
|-------|-------------|------------------|--------|----------|
| **Phase I** | In-Memory Python Console App | Python, Claude Code, Spec-Kit Plus | — | — |
| **Phase II** | Full-Stack Web Application | Next.js, FastAPI, SQLModel, Neon DB | — | — |
| **Phase III** | AI-Powered Todo Chatbot | OpenAI ChatKit, Agents SDK, Official MCP SDK | — | — |
| **Phase IV** | Local Kubernetes Deployment | Docker, Minikube, Helm, kubectl-ai, kagent | — | Jan 4, 2026 |
| **Phase V** | Advanced Cloud Deployment | Kafka, Dapr, DigitalOcean DOKS | — | — |

---

## 🚀 Quick Start

Each phase builds upon the previous one. Follow the documentation for each phase:

- **Phase I:** Console-based prototyping (baseline functionality)
- **Phase II:** Web UI + REST API + Database persistence
- **Phase III:** AI chatbot integration with Claude/OpenAI
- **Phase IV:** Containerization and local Kubernetes orchestration
- **Phase V:** Production-grade event-driven architecture on cloud Kubernetes

---

## 📂 Project Structure

```
HackathonIIphase4amna/
├── backend/                  # FastAPI backend service
├── frontend/                 # Next.js frontend application
├── notification-service/     # Event-driven notification microservice
├── k8s/                       # Kubernetes manifests

├── specs/                     # Specification documents
├── history/prompts/           # Phase-specific documentation 
```

---

## 🛠️ Technology Highlights

### Backend
- **FastAPI** (Python 3.11+) with async support
- **SQLModel** for ORM and type safety
- **Neon PostgreSQL** for serverless database

### Frontend
- **Next.js 14+** with server components
- **Shadcn/UI** for accessible components
- **Better Auth** for authentication

### AI & Intelligence
- **Google Gemini** LLM for conversational AI
- **Model Context Protocol (MCP)** for tool-driven AI behavior
- **Dapr** for infrastructure abstraction

### Infrastructure
- **Docker** with multi-stage builds
- **Kubernetes** (Minikube for dev, DOKS/AKS/GKE for prod)
- **Kafka/Redpanda** for event streaming

---

## 📖 Documentation

- **Constitution:** `.specify/memory/constitution.md` — Governance rules for all phases
- **Implementation Guides:** `history/prompts/phase*/` — Detailed implementation instructions

---

## ✅ Status

- ✅ Phase I-IV: Completed
- 🔄 Phase V: Completed

---

**Ratified:** February 7, 2026 
## **Managed By Aamna Ansari**
