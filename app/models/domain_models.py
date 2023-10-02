from dataclasses import dataclass
from pydantic import BaseModel
from typing import Any, Dict, List, Optional

@dataclass
class Actor(BaseModel):
    id: str
    type: str = "Person"
    inbox: str
    outbox: str
    # ... any other actor fields

@dataclass
class Activity(BaseModel):
    id: str
    type: str
    actor: str
    object: Dict[str, Any]
    # ... other activity fields

@dataclass
class WebfingerLink(BaseModel):
    rel: str
    type: Optional[str]
    href: str

@dataclass
class WebfingerResponse(BaseModel):
    subject: str
    aliases: List[str]
    links: List[WebfingerLink]

class NodeinfoWellKnown(BaseModel):
    links: List[Dict[str, str]]

class Nodeinfo(BaseModel):
    version: str
    software: Dict[str, str]
    protocols: List[str]
    services: Dict[str, List[str]]
    openRegistrations: bool
    usage: Dict[str, int]