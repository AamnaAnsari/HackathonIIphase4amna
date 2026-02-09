# Phase 5 Implementation Details: Advanced Cloud & Event-Driven Architecture

This document summarizes the technical implementation of Phase 5, focusing on distributed systems, event-driven logic, and cloud-native orchestration.

## 1. Data Layer Enhancements (backend/models.py)

We upgraded the Task model to support enterprise-level features.

```python
from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import List, Optional
import json

class Task(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    description: Optional[str] = None
    status: str = Field(default="pending")
    priority: str = Field(default="Medium") # High, Medium, Low
    tags: str = Field(default="[]")         # Stored as JSON string
    due_date: Optional[datetime] = None
    user_id: str
```

## 2. Dapr Pub/Sub Configuration (dapr/components/pubsub.yaml)

This component connects our microservices to Redpanda Cloud (Kafka).

```yaml
apiVersion: dapr.io/v1alpha1
kind: Component
metadata:
  name: task-pubsub
spec:
  type: pubsub.kafka
  version: v1
  metadata:
  - name: brokers
    value: "${REDPANDA_BROKERS}"
  - name: authRequired
    value: "true"
  - name: saslUsername
    value: "${REDPANDA_USER}"
  - name: saslPassword
    value: "${REDPANDA_PASSWORD}"
  - name: saslMechanism
    value: "SCRAM-SHA-256"
```

## 3. Event Publisher Logic (backend/main.py)

The backend now emits events asynchronously whenever a task is manipulated.

```python
from dapr.clients import DaprClient

async def publish_task_event(task_data: dict):
    with DaprClient() as client:
        client.publish_event(
            pubsub_name='task-pubsub',
            topic_name='task-events',
            data=json.dumps(task_data),
            data_content_type='application/json',
        )
```

## 4. Notification Service (src/notification-service/main.py)

A standalone microservice that reacts to events without direct API dependency.

```python
from fastapi import FastAPI
from dapr.ext.fastapi import DaprApp

app = FastAPI()
dapr_app = DaprApp(app)

@dapr_app.subscribe(pubsub_name='task-pubsub', topic='task-events')
def task_event_handler(event_data):
    # Logic to handle notifications (e.g., logging or sending emails)
    print(f"🔔 Notification Received: {event_data.data}")
```

## 5. Kubernetes Orchestration (k8s/backend-deploy.yaml)

Deployment with Dapr Sidecar Injection for cloud-native portability.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: todo-backend
spec:
  template:
    metadata:
      annotations:
        dapr.io/enabled: "true"
        dapr.io/app-id: "backend-api"
        dapr.io/app-port: "8000"
    spec:
      containers:
      - name: backend
        image: ghcr.io/username/todo-backend:latest
        ports:
        - containerPort: 8000
```

## 6. Infrastructure Verification Summary

- **Messaging:** Verified via Redpanda Console (Messages are flowing).
- **Discovery:** Dapr sidecars communicate over gRPC.
- **Auth:** JWT validation implemented in both microservices.
- **Statelessness:** No local session data; all state in NeonDB or Dapr State Store.
