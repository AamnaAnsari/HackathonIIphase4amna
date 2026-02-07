# Phase 5 Execution Tasks

## Stage 1: Advanced Features Implementation

- [ ] **Task-1.1:** Update SQLModel Task schema in `backend/models.py` (Add: priority, tags, due_date, recurrence).

- [ ] **Task-1.2:** Generate migration script or `reset_db.py` to update NeonDB schema.

- [ ] **Task-1.3:** Update `backend/mcp_tools.py` to expose new fields to the AI Agent (e.g., `add_task` accepts priority/due_date).

- [ ] **Task-1.4:** Implement Search & Filter logic in `backend/main.py` (GET /tasks?q=...&priority=...).

## Stage 2: Dapr & Event-Driven Setup

- [ ] **Task-2.1:** Add `dapr-ext-fastapi` and `cloudevents` to `backend/requirements.txt`.

- [ ] **Task-2.2:** Create `k8s/dapr/components/pubsub.yaml` (Kafka/Redpanda configuration).

- [ ] **Task-2.3:** Create `k8s/dapr/components/statestore.yaml` (Redis configuration).

- [ ] **Task-2.4:** Refactor `backend/main.py` to publish `task.created` and `task.completed` events via Dapr Client.

## Stage 3: Microservices Development

- [ ] **Task-3.1:** Create folder `notification_service/`.

- [ ] **Task-3.2:** Implement `notification_service/main.py` (FastAPI) that subscribes to task-events via Dapr.

- [ ] **Task-3.3:** Create `notification_service/Dockerfile`.

## Stage 4: Kubernetes Orchestration (Local)

- [ ] **Task-4.1:** Update `k8s/backend-deployment.yaml` to include Dapr annotations (`dapr.io/enabled: "true"`).

- [ ] **Task-4.2:** Create `k8s/notification-deployment.yaml`.

- [ ] **Task-4.3:** Create `deploy_local.sh` script to apply Dapr components and K8s manifests to Minikube.

## Stage 5: Cloud Deployment & CI/CD

- [ ] **Task-5.1:** Create `.github/workflows/build-push.yml` to build images and push to GitHub Container Registry.

- [ ] **Task-5.2:** Create `.github/workflows/deploy-k8s.yml` to deploy to AKS/GKE.

- [ ] **Task-5.3:** Set up Cloud Secrets (NeonDB URL, Gemini Key, Redpanda Creds) in GitHub Secrets.

## Verification

- [ ] **Verify-1:** User can say "Remind me to sleep in 1 minute" -> Event published -> Notification Service logs it.

- [ ] **Verify-2:** Cloud URL works publicly with full persistence.
