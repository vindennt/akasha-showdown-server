# Adapted from https://github.com/AtticusZeller/fastapi_supabase_template?tab=readme-ov-file

import uuid

from sqlmodel import SQLModel, Field
from pydantic import EmailStr

class User(SQLModel, table=True):
    """WARNING: Don't migrate this using alembic, it should already exist in the default supabase configuration."""

    __tablename__ = "users"
    __table_args__ = {"schema": "auth", "keep_existing": True}

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(max_length=255)