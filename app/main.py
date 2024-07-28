from fastapi import FastAPI
from app.routes import auth, alert, price
from app.utils.websocket import start_websocket
from app.utils.db import engine, Base

app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(alert.router, prefix="/alerts", tags=["alerts"])
app.include_router(price.router, prefix="/price", tags=["price"])
app.get("/")(lambda: {"message": "Hey! This is Sai Sahith Bonugala (21BIT0175) from Vellore Institute of Technology, VIT"})

Base.metadata.create_all(bind=engine)

start_websocket()
