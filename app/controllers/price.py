from fastapi import HTTPException
import requests

def get_current_price():
    coin = "BTCUSDT"
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={coin}"
    response = requests.get(url)
    data = response.json()
    current_price = float(data['price'])
    return current_price