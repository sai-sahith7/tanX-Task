from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.alert import create_alert, delete_alert, get_alerts, get_alertsById
from app.utils.db import get_db
from app.utils.jwt import get_current_user
from app.models.user import User
from app.schemas.alert import Alert


router = APIRouter()

@router.get("/")
def get_alerts_route(skip: int = 0, limit: int = 10, status: str = None, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_alerts(skip, limit, status, db, user)

@router.get("/id")
def get_alerts_id_route(id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_alertsById(id, db, user)

@router.get("/created")
def get_created_alerts_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_alerts(skip, limit, "created", db, user)

@router.get("/triggered")
def get_triggered_alerts_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_alerts(skip, limit, "triggered", db, user)

@router.get("/deleted")
def get_deleted_alerts_route(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return get_alerts(skip, limit, "deleted", db, user)

@router.post("/create")
def create_alert_route(alert: Alert, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return create_alert(alert.coin, alert.target_price, db, user) #because currently we are only focussed on Bitcoin

@router.delete("/delete")
def delete_alert_route(id: int, db: Session = Depends(get_db), user: User = Depends(get_current_user)):
    return delete_alert(id, db, user)


