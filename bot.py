import websocket
import json
import pprint

# See: https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md#klinecandlestick-streams

# Stream name <symbol><stream><interval>
# SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"
SOCKET = "wss://stream.binance.com:9443/ws/dogeusdt@kline_1m"

closes = []


def on_message(ws, message):
    global closes
    print("received message")
    json_message = json.loads(message)
    pprint.pprint(json_message)

    candle = json_message["k"]
    is_candle_closed = candle["x"]
    close = candle["c"]

    if is_candle_closed:
        print("Candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)


def on_error(ws, error):
    print("received error", error)


def on_close(ws):
    print("closed connection")


def on_open(ws):
    print("opened connection")


ws = websocket.WebSocketApp(SOCKET,
                            on_open=on_open,
                            on_close=on_close,
                            on_message=on_message,
                            on_error=on_error)

ws.run_forever()
