from fastapi import FastAPI
from app.routers.event_router import router as event_router

app = FastAPI(title="Event API")

app.include_router(event_router)