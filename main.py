from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.actor_routes import router as actor_routes
from app.routers.ai_routes import router as ai_routes
from app.services.database import client
from app.core.config import DATABASE_NAME

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

@app.on_event("startup")
async def startup_db_client():
    if client is not None:
        app.mongodb = client[DATABASE_NAME]


@app.on_event("shutdown")
async def shutdown_db_client():
    if client is not None:
        client.close()
