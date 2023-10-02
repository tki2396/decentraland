from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Any, Dict
from app.models.domain_models import Activity, Actor
import app.services.user_service as user_service_module


router = APIRouter()

def get_user_service():
    return user_service_module

@router.post("/users/")
async def create_user(user: Actor, user_service: user_service_module = Depends(get_user_service)):
    await user_service.create_user(user)
    return {"message": "User created successfully"}


@router.get("/users/{username}/outbox", response_model=Activity)
async def read_outbox(username: str, user_service: user_service_module = Depends(get_user_service)):
    await user_service.read_outbox(username)
    return {"message": "User created successfully"}

@router.post("/users/{username}/inbox")
async def receive_activity(activity: Activity, user_service: user_service_module = Depends(get_user_service)):
    await user_service.receive_activity(activity)
    return {"message": "User created successfully"}
    
@router.post("/users/create")
async def make(actor: Actor, user_service: user_service_module = Depends(get_user_service)):
    await user_service.make(actor)
    return {"message": "User created successfully"}