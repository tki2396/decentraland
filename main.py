from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.routers.actor_routes import router as actor_routes
from app.routers.ai_routes import router as ai_routes


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(actor_routes)
app.include_router(ai_routes)


DATABASE_URL = "mongodb://localhost:27017"
DATABASE_NAME = "activitypub"

client: AsyncIOMotorClient = None


def get_db() -> AsyncIOMotorDatabase:
    return app.mongodb


@app.on_event("startup")
async def startup_db_client():
    global client
    client = AsyncIOMotorClient(DATABASE_URL)
    app.mongodb = client[DATABASE_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    global client
    if client:
        client.close()
