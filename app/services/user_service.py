from app.models.domain_models import Actor, Activity
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from fastapi import APIRouter, Depends, HTTPException
from app.services.database import user_collection

client = AsyncIOMotorClient("mongodb://localhost:27017")


async def get_motor_client():
    return client

async def create_user(user: Actor, client: AsyncIOMotorClient = Depends(get_motor_client)):
    user_collection.insert_one(user.model_dump())
    return {"message": "User created successfully"}

# @app.get("/users/{username}/outbox", response_model=Activity)
async def read_outbox(username: str, db: AsyncIOMotorDatabase = Depends(get_motor_client)):
    outbox_data = await db["outbox"].find_one({"actor": f"http://example.com/users/{username}"})
    if not outbox_data:
        raise HTTPException(status_code=404, detail="Outbox not found")
    return outbox_data

# @app.post("/users/{username}/inbox")
async def receive_activity(activity: Activity, db: AsyncIOMotorDatabase = Depends(get_motor_client)):
    # You would validate the activity, authenticate the request, etc. here.
    # For simplicity, this example just stores it.
    result = await db["inbox"].insert_one(activity.dict())
    if result.acknowledged:
        return {"status": "activity received"}
    else:
        raise HTTPException(status_code=500, detail="Activity reception failed")
    
# @app.post("/users/create")
async def make(actor: Actor, db: AsyncIOMotorDatabase = Depends(get_motor_client)):
    result = await db["actors"].insert_one(actor.dict())
    if result.acknowledged:
        return {"status": "actor created"}
    else:
        raise HTTPException(status_code=500, detail="Actor creation failed")
