from app.models.domain_models import Actor
from motor.motor_asyncio import AsyncIOMotorCollection
from fastapi import Depends
from app.core.database import user_collection

async def get_user_collection():
    return user_collection

class UserService:

    def __init__(self, user_collection: AsyncIOMotorCollection):
        self.user_collection = user_collection


    async def create_user(self, user: Actor):
        user_collection.insert_one(user.model_dump())
        return {"message": "Actor created successfully"}

    async def delete_user(self, username: str):
        self.user_collection.delete_one({"username": username})
        return {"message": "User deleted successfully"}

    async def get_all_actor(self):
        actors = await self.user_collection.find().to_list(length=100)  # or adjust length as needed
        for actor in actors:
            actor["_id"] = str(actor["_id"])
        return actors

async def get(user_collection: AsyncIOMotorCollection = Depends(get_user_collection)) -> UserService:
    return UserService(user_collection)