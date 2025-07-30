from sqlmodel import SQLModel, Field
from typing import Optional
import uuid

class User(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default_factory=uuid.uuid4, primary_key=True)
    email: str = Field(index=True, unique=True, nullable=False)
    username: Optional[str]
    wins: int = Field(default=0, nullable=False)
    losses: int = Field(default=0, nullable=False)