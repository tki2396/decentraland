from app.models.domain_models import Activity
from motor.motor_asyncio import AsyncIOMotorCollection
from fastapi import Depends, HTTPException
from app.core.database import activity_collection


async def get_activity_collection():
    return activity_collection


async def read_outbox(username: str, db: AsyncIOMotorCollection = Depends(get_activity_collection)):
    outbox_data = await db["outbox"].find_one({"actor": f"http://example.com/users/{username}"})
    if not outbox_data:
        raise HTTPException(status_code=404, detail="Outbox not found")
    return outbox_data

async def receive_activity(activity: Activity, db: AsyncIOMotorCollection = Depends(get_activity_collection)):
    # You would validate the activity, authenticate the request, etc. here.
    # For simplicity, this example just stores it.
    result = await db["inbox"].insert_one(activity.dict())
    if result.acknowledged:
        return {"status": "activity received"}
    else:
        raise HTTPException(status_code=500, detail="Activity reception failed")