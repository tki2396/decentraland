from pydantic import BaseModel
from typing import Any, Dict

class Actor(BaseModel):
    id: str
    type: str = "Person"
    inbox: str
    outbox: str
    # ... any other actor fields

class Activity(BaseModel):
    id: str
    type: str
    actor: str
    object: Dict[str, Any]
    # ... other activity fields