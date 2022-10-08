import json,config
from binance.client import Client
from binance.enums import *
from flask import Flask,request
app=Flask(__name__)

client=Client(config.PASSPHRASE,config.API_KEY,config.API_PASS)

def order(side,quantity,symbol,order_type=ORDER_TYPE_MARKET):
    try:
        print(f"Order submitted {side}---{quantity}---{symbol}---{order_type}")
        order=client.create_order(side=side,quantity=quantity,symbol=symbol,order_type=order_type)
    except Exception as e:
        print(f"ERROR {e}")
        return False
    return order
@app.route('/webhook',methods=["POST"])

def webhook():
    data=json.loads(request.data)
    if data['passphrase'] !=config.PASSPHRASE:
        return {
            "code":"ERROR",
            "message":"WRONG PASS"
        }
    print(request.data)
    return {
        "code":"success",
        "message":data
    }

