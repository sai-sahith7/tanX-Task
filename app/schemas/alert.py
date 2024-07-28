from pydantic import BaseModel

class Alert(BaseModel):
    coin: str = "BTCUSDT"
    target_price: float
    status: str = 'created'