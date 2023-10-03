from fastapi import APIRouter, Depends
from app.models.domain_models import Actor
from app.actors.actor_service import UserService, get


router = APIRouter()

def get_user_service():
    return UserService()

@router.post("/users/")
async def create_user(user: Actor, user_service: UserService = Depends(get)):
    await user_service.create_user(user)
    return {"message": "User created successfully"}

@router.delete("/users/{username}")
async def delete_user(username: str, user_service: UserService = Depends(get)):
    await user_service.delete_user(username)
    return {"message": "User deleted successfully"}

    
@router.get("/users/")
async def list_users(user_service: UserService = Depends(get)):
    users = await user_service.get_all_actor()
    return users