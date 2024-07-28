import websocket
import json
from sqlalchemy.orm import Session
from app.utils.db import SessionLocal
from app.models.alert import Alert
from app.utils.email import send_email

def on_message(ws, message):
    data = json.loads(message)
    price = float(data['k']['c'])
    coin = data['s']
    db: Session = SessionLocal()
    alerts = db.query(Alert).filter(Alert.coin == coin, Alert.status == "created").all()
    for alert in alerts:
        if ( alert.price_when_created <= alert.target_price and alert.target_price <= price):
            alert.status = "triggered"
            db.commit()
            send_email(alert.owner.email, "Price Alert", f"The price of {alert.coin} has reached {alert.target_price}. You created this alert when the price was {alert.price_when_created}. \n\nThe current BTC price is {price}.")
        elif (alert.price_when_created >= alert.target_price and alert.target_price >= price):
            alert.status = "triggered"
            db.commit()
            send_email(alert.owner.email, "Price Alert", f"The price of {alert.coin} has reached {alert.target_price}. You created this alert when the price was {alert.price_when_created}. \n\nThe current BTC price is {price}.")
    db.close()

def on_error(ws, error):
    print(error)

def on_close(ws, close_msg):
    print("*** Web socket closed ***" + close_msg)

def start_websocket():
    def run_websocket():
        websocket.enableTrace(False)
        socket = 'wss://stream.binance.com:9443/ws/btcusdt@kline_1m'
        ws = websocket.WebSocketApp(socket, on_message=on_message, on_error=on_error, on_close=on_close)
        ws.run_forever()

    import threading
    websocket_thread = threading.Thread(target=run_websocket)
    websocket_thread.start()
