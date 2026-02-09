# Phase 5 Execution Tasks: Advanced Cloud & Event-Driven Architecture

## Stage 1: Core Logic & AI Integration

- [ ] **T-5.1.1: Update Data Models**

  - **Description:** Add `priority`, `tags`, and `due_date` fields to the `Task` class in `src/backend/models.py`.
  - **Verification:** Run `python -c "from models import Task; print(Task.__fields__)"` to see new fields.

- [ ] **T-5.1.2: Neon DB Migration**

  - **Description:** Run the SQL migration or update script to reflect schema changes in Neon PostgreSQL.
  - **Verification:** Check Neon Console tables for new columns.

- [ ] **T-5.1.3: Update Gemini MCP Tools**

  - **Description:** Modify `add_task` and `update_task` in `src/backend/mcp_tools.py` to accept and process `priority` and `tags` from Gemini.
  - **Verification:** Ask Gemini: "Add an urgent task tagged as work" and check if fields are populated in DB.

- [ ] **T-5.1.4: Implement Advanced Search**

  - **Description:** Update `src/backend/main.py` with a search endpoint that supports keyword, tag, and priority filtering.
  - **Verification:** Call `GET /tasks?priority=High` and verify filtered results.

## Stage 2: Event-Driven Setup (Dapr + Redpanda)

- [ ] **T-5.2.1: Create Dapr Pub/Sub Component**

  - **File:** `dapr/components/pubsub.yaml`
  - **Description:** Configure Dapr to use Redpanda Cloud with SASL_SSL credentials.
  - **Verification:** Run `dapr components` to ensure `task-pubsub` is loaded.

- [ ] **T-5.2.2: Implement Backend Publisher**

  - **File:** `src/backend/main.py`
  - **Description:** Use Dapr Python SDK to publish a `task.created` event whenever a task is successfully added.
  - **Verification:** Check Dapr sidecar logs for successful publishing.

## Stage 3: Notification Microservice Development

- [ ] **T-5.3.1: Initialize Notification Service**

  - **File:** `src/notification-service/main.py`
  - **Description:** Setup a new FastAPI service using `dapr-ext-fastapi`.
  - **Verification:** Service starts on port `8001`.

- [ ] **T-5.3.2: Implement Event Subscriber**

  - **File:** `src/notification-service/main.py`
  - **Description:** Add `@app.subscribe` handler for the `task.reminder` topic.
  - **Verification:** Create a task with a reminder and check if Notification Service receives the event.

## Stage 4: Containerization & Infrastructure

- [ ] **T-4.1.1: Multi-Stage Dockerfiles**

  - **Files:** `src/backend/Dockerfile`, `src/notification-service/Dockerfile`
  - **Description:** Create optimized Docker images for both services.
  - **Verification:** Run `docker build` and verify image size is < 200MB.

- [ ] **T-4.2.1: Kubernetes Manifests**

  - **Files:** `k8s/backend-deploy.yaml`, `k8s/notification-deploy.yaml`
  - **Description:** Define K8s Deployments with Dapr annotations (`dapr.io/enabled: "true"`).
  - **Verification:** Run `kubectl apply` and check if pods start with `2/2` containers (App + Sidecar).

## Stage 5: Deployment & CI/CD

- [ ] **T-5.1.1: GitHub Actions Workflow**

  - **File:** `.github/workflows/deploy.yml`
  - **Description:** Create a pipeline to build images and push them to GHCR.
  - **Verification:** Push code and verify "Green Tick" on GitHub Actions tab.

- [ ] **T-5.1.2: Cloud Secret Injection**

  - **Description:** Configure K8s secrets for Neon DB, Redpanda, and Gemini API Keys on the cloud cluster.
  - **Verification:** Log into a pod and run `env` to see if secrets are injected.

## ✅ Final Verification (End-to-End)

- [ ] **Verification:** Send a chat message -> Gemini creates task -> Event published to Redpanda -> Notification Service logs the receipt.
