from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.utils.jwt import create_access_token
from app.utils.hash import get_password_hash, verify_password
from app.models.user import User
from app.utils.email import send_email

def register_user(email: str, password: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = get_password_hash(password)
    new_user = User(email=email, hashed_password=hashed_password)
    send_email(email, "Welcome to Alerts API!", "Thank you for signing up! You can now create alerts to get notified when the price of BTC reaches a certain value. \n\nSai Sahith Bonugala\nVellore Institute of Technology \n21BIT0175")
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"user_id": new_user.id, "email_id": new_user.email, "message": "User created successfully! You should have received a welcome email. Please check your inbox. If you can't find it, please check your spam folder."}

def login_user(email:str, password:str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token}
