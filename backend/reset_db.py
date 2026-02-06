"""
Reset database script: drops and recreates all tables.
Run this to start fresh with the database schema.
"""
from sqlmodel import SQLModel

from database import engine
from models import Conversation, Message, Task, User  # noqa: F401

if __name__ == "__main__":
    print("Dropping all tables...")
    SQLModel.metadata.drop_all(engine)
    
    print("Creating all tables...")
    SQLModel.metadata.create_all(engine)
    
    print("✅ Database reset complete!")
    print("Tables created: users, tasks, conversations, messages")
