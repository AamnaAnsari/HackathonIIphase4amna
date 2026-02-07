# Phase 5 Implementation Guide

## A. Database Schema Update (backend/models.py)

```python
class Task(SQLModel, table=True):
    # ... existing fields ...
    priority: str = Field(default="Medium")  # High, Medium, Low
    tags: str = Field(default="[]")          # JSON string of tags
    due_date: datetime | None = None
    is_recurring: bool = False
    recurrence_interval: str | None = None   # e.g., "daily", "weekly"
```

## B. Dapr Component: Pub/Sub (k8s/dapr/components/pubsub.yaml)

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
    value: "REDPANDA_BROKER_URL"
  - name: authRequired
    value: "true"
  - name: saslUsername
    value: "USER"
  - name: saslPassword
    secretKeyRef:
      name: redpanda-secret
      key: password
```

## C. Backend Dapr Integration (backend/main.py)

```python
from dapr.ext.fastapi import DaprApp
app = FastAPI()
dapr_app = DaprApp(app)

@app.post("/tasks")
async def create_task(task: TaskCreate):
    # ... save to DB ...
    # Publish Event via Dapr Sidecar
    await dapr_app.pubsub.publish(
        pubsub_name="task-pubsub",
        topic_name="task-events",
        data_content_type="application/json",
        data=task.json()
    )
```

## D. Notification Service Subscriber (notification_service/main.py)

```python
from fastapi import FastAPI
from cloudevents.sdk.event import v1
from dapr.ext.fastapi import DaprApp

app = FastAPI()
dapr_app = DaprApp(app)

# Subscribe to the topic
@dapr_app.subscribe(pubsub_name="task-pubsub", topic="task-events")
def event_handler(event: v1.Event):
    print(f"🔔 Received Event: {event.Data()}")
    # Logic to send email/push notification goes here
```

## E. Kubernetes Deployment with Dapr (k8s/backend-deployment.yaml)

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: backend
spec:
  template:
    metadata:
      annotations:
        dapr.io/enabled: "true"
        dapr.io/app-id: "backend"
        dapr.io/app-port: "8000"
        dapr.io/config: "appconfig"
# ... rest of deployment configuration
```
