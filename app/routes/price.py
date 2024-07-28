from fastapi import APIRouter, Depends
from app.controllers.price import get_current_price
from app.models.user import User
from app.utils.jwt import get_current_user

router = APIRouter()

@router.get("/")
def get_price(user: User = Depends(get_current_user)):
    return {"price": get_current_price()}