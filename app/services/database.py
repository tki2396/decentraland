from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import MONGODB_URI

client = AsyncIOMotorClient(MONGODB_URI)
database = client.get_database('activitypub')  # Replace 'mydatabase' with your database name

user_collection = database.get_collection("users")