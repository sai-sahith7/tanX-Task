from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.controllers.auth import register_user, login_user
from app.utils.db import get_db
from app.schemas.user import User

router = APIRouter()

@router.post("/register")
def register(user: User, db: Session = Depends(get_db)):
    return register_user(user.email, user.password, db)

@router.post("/login")
def login(user: User, db: Session = Depends(get_db)):
    return login_user(user.email,user.password, db)
