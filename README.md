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


🏗️ Project Architecture Evolution (Phase 1 - 5)

Our journey from a simple local script to a professional Cloud-Native system:

---

graph TD
    %% Phase 1 & 2 (Foundation)
    subgraph P1_P2 [Phase 1 & 2: Local Foundation]
        A[models.py] --- B[manager.py]
        B --- C[(Local SQLite/Files)]
    end

    %% Phase 3 (Web/API)
    subgraph P3 [Phase 3: Conversational AI]
        D[Next.js UI] -- HTTP/JWT -- E[FastAPI Backend]
        E -- Tool Calling -- F((Google Gemini AI))
        E -- SQL -- G[(NeonDB Cloud)]
    end

    %% Phase 4 (Containerization)
    subgraph P4 [Phase 4: Orchestration]
        H[Docker: Frontend] --- I[Docker: Backend]
        I --- J[Minikube/Local K8s]
    end

    %% Phase 5 (Cloud Native & Events)
    subgraph P5 [Phase 5: Event-Driven Cloud]
        K[Vercel UI] -- HTTPS -- L[HF Spaces: Backend API]
        L -- Dapr Sidecar -- M{Redpanda Cloud / Kafka}
        M -- Topic: task-events -- N[Notification Microservice]
        L -- SQL -- O[(NeonDB Serverless)]
        L -- Dapr State -- P[Redis State Store]
    end

    %% Evolution Flow
    P1_P2 ==> P3
    P3 ==> P4
    P4 ==> P5

    style P5 fill:#f9f,stroke:#333,stroke-width:4px
    style K fill:#fff,stroke:#333
    style L fill:#fff,stroke:#333
    style M fill:#ff9,stroke:#f66,stroke-width:2px
    
---


## ✅ Status

- ✅ Phase I-IV: Completed
- ✅ Phase V: Completed

---

**Ratified:** February 7, 2026 
## **Managed By Aamna Ansari**
