from fastapi import FastAPI, Depends
from app.routers.event_router import router as event_router
from app.routers.auth_router import router as auth_router
from app.routers.booking_router import router
from app.routers.payment_router import router as payment_router
from app.routers.ticket_router import router as ticket_router
from app.routers.ticket_type_router import router as ticket_type_router


from app.database import Base, engine, get_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Event API")



app.include_router(event_router)
app.include_router(auth_router)
app.include_router(router)
app.include_router(ticket_router)
app.include_router(ticket_type_router)
app.include_router(payment_router)