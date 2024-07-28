from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.models.alert import Alert
from app.models.user import User
from app.models.log import Log
import requests

def create_alert(coin: str, target_price: float, db: Session, user: User):
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}"
    response = requests.get(url)
    data = response.json()
    current_price = float(data['price'])
    alert = Alert(owner_id=user.id, coin=coin, target_price=target_price, price_when_created=current_price, status="created")
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert

def delete_alert(alert_id: int, db: Session, user: User):
    alert = db.query(Alert).filter(Alert.id == alert_id, Alert.owner_id == user.id).first()
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    log = Log(owner_id=user.id, coin = alert.coin, target_price = alert.target_price, price_when_created = alert.price_when_created, status="deleted")
    db.add(log)
    db.delete(alert)
    db.commit()
    return {"detail": "Alert deleted"}

def get_alerts(skip: int, limit: int, status: str, db: Session, user: User):
    query = db.query(Alert).filter(Alert.owner_id == user.id)
    if status:
        if status not in ["created", "triggered", "deleted"]:
            raise HTTPException(status_code=400, detail="Invalid status")
        if status == "deleted":
            delete_query = db.query(Log).filter(Log.owner_id == user.id)
            alerts = delete_query.offset(skip).limit(limit).all()
            print("delete_query", delete_query)
            return alerts
        query = query.filter(Alert.status == status)
    alerts = query.offset(skip).limit(limit).all()
    return alerts

def get_alertsById(id: int, db: Session, user: User):
    alert = db.query(Alert).filter(Alert.id == id, Alert.owner_id == user.id).first()
    if not alert:
        check = db.query(Alert).filter(Alert.id == id).first()
        if check:
            raise HTTPException(status_code=403, detail="Unauthorized")
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert
