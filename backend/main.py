"""
FastAPI app per specs/api/rest-endpoints.md and backend/CLAUDE.md.
Routes under /api/, JSON responses. Dummy auth for now.
"""
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # <-- 1. Import Added
from pydantic import BaseModel
from sqlmodel import Session, select

from chat_agent import get_gemini_response
from database import engine, get_session
from models import Conversation, Message, SQLModel, Task, User  # noqa: F401

app = FastAPI(title="Todo API", version="1.0")

# --- 2. Middleware Added Here ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL allowed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, PUT, DELETE, OPTIONS)
    allow_headers=["*"],  # Allow all headers
)
# --------------------------------

app.state.engine = engine


@app.on_event("startup")
def on_startup():
    """Create database tables on startup."""
    SQLModel.metadata.create_all(engine)


def dummy_auth() -> None:
    """Dummy auth: no-op for testing. Replace with JWT verification later."""
    pass


class TaskCreate(BaseModel):
    """Request body for creating a task (title required, 1-200 chars)."""
    title: str
    completed: bool = False


class ChatRequest(BaseModel):
    """Request body for chat endpoint."""
    user_id: str
    message: str


@app.get("/api/{user_id}/tasks")
def list_tasks(
    user_id: str,
    session: Session = Depends(get_session),
    _auth: None = Depends(dummy_auth),
):
    """GET /api/{user_id}/tasks - list tasks for user (dummy auth)."""
    statement = select(Task).where(Task.user_id == user_id)
    tasks = session.exec(statement).all()
    # model_dump is the new Pydantic v2 method (was .dict())
    return [t.model_dump() for t in tasks]


@app.post("/api/{user_id}/tasks")
def create_task(
    user_id: str,
    body: TaskCreate,
    session: Session = Depends(get_session),
    _auth: None = Depends(dummy_auth),
):
    """POST /api/{user_id}/tasks - create task (dummy auth)."""
    if not body.title or len(body.title) > 200:
        raise HTTPException(status_code=400, detail="Title required (1-200 chars)")
    
    # Create Task object
    task = Task(user_id=user_id, title=body.title, completed=body.completed)
    session.add(task)
    session.commit()
    session.refresh(task)
    return task.model_dump()


@app.put("/api/{user_id}/tasks/{task_id}")
def update_task(
    user_id: str,
    task_id: int,
    body: TaskCreate,
    session: Session = Depends(get_session),
    _auth: None = Depends(dummy_auth),
):
    """PUT /api/{user_id}/tasks/{task_id} - update task (dummy auth)."""
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")
    if not body.title or len(body.title) > 200:
        raise HTTPException(status_code=400, detail="Title required (1-200 chars)")
    task.title = body.title
    task.completed = body.completed
    session.add(task)
    session.commit()
    session.refresh(task)
    return task.model_dump()


@app.delete("/api/{user_id}/tasks/{task_id}")
def delete_task(
    user_id: str,
    task_id: int,
    session: Session = Depends(get_session),
    _auth: None = Depends(dummy_auth),
):
    """DELETE /api/{user_id}/tasks/{task_id} - delete task (dummy auth)."""
    task = session.get(Task, task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.user_id != user_id:
        raise HTTPException(status_code=404, detail="Task not found")
    session.delete(task)
    session.commit()
    return {"message": "Task deleted"}


@app.post("/api/chat")
def chat(
    body: ChatRequest,
    _auth: None = Depends(dummy_auth),
):
    """POST /api/chat - send a message to the Gemini chatbot; returns the AI response text."""
    with Session(engine) as session:
        response_text = get_gemini_response(body.user_id, body.message, session)
    return {"response": response_text}


@app.get("/")
def root():
    """Health/root."""
    return {"message": "Todo API", "docs": "/docs"}