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


### 🌐 System Architecture Diagram

```mermaid
graph TD
    User((User)) -- HTTPS/Vercel --> FE[Next.js Frontend]
    FE -- JWT/Auth --> BE[FastAPI Backend - HF Spaces]
    
    subgraph "The Brain"
        BE -- Model Context Protocol --> Gemini((Google Gemini))
        Gemini -- Tools --> CRUD[MCP CRUD Tools]
    end
    
    subgraph "Infrastructure Layer (Dapr)"
        BE -- gRPC --> DaprSidecar[Dapr Sidecar]
        DaprSidecar -- Pub/Sub --> Kafka[Redpanda Cloud]
    end
    
    subgraph "Persistence"
        CRUD -- SQL --> Neon[(Neon PostgreSQL)]
        DaprSidecar -- State --> Redis[Redis State Store]
    end
    
    subgraph "Microservices"
        Kafka -- Topic: task-events --> NS[Notification Service]
        NS -- Sidecar --> Logs((Reminders/Logs))
    end

### Explanation of the Diagram:
1.  **Vercel & Next.js:** This is your entrance gate where the user interacts.
2.  **Hugging Face & FastAPI:** This is the core logic. It’s stateless, meaning it doesn't store anything on the disk, making it fast and scalable.
3.  **Dapr Sidecar:** This is the bridge you built. It allows your backend to talk to Kafka (Redpanda) without needing heavy Kafka drivers in your code.
4.  **Redpanda Cloud:** This is your message broker. It handles the "Events" (like Task Created) so the Notification service can react to them later.
5.  **NeonDB:** Your serverless database that holds all the truth (Tasks & Chat history).

---


## ✅ Status

- ✅ Phase I-IV: Completed
- ✅ Phase V: Completed

---

**Ratified:** February 7, 2026 
## **Managed By Aamna Ansari**
