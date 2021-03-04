import config
from binance.client import Client
from binance.enums import *

TRADE_SYMBOL = 'DOGEUSDT'
TRADE_QUANTITY = 250

client = Client(config.API_KEY, config.API_SECRET)

def order():
    try:
        order = client.create_order(symbol=TRADE_SYMBOL, side=SIDE_BUY, type=ORDER_TYPE_MARKET, quantity=TRADE_QUANTITY)
        print("order")
        print(order)
    except Exception as e:
        print(e)

order()