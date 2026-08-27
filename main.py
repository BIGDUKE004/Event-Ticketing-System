from fastapi import FastAPI
from app.routers.event_router import router as event_router
from app.routers.auth_router import router as auth_router
from app.routers.booking_router import router

app = FastAPI(title="Event API")

app.include_router(event_router)
app.include_router(auth_router)
app.include_router(router)