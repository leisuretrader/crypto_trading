import websocket, json

def on_open(ws):
    print ('the socket is opened')
    # subcribe_message = {
    # "method": "SUBSCRIBE",
    # "params":
    # [
    # "btcusdt@aggTrade",
    # "btcusdt@depth"
    # ],
    # "id": 1
    # }
    # ws.send(json.dumps(subcribe_message))

def on_message(ws, message):
    print (message)
    # current_data = json.loads(message)
    # print (current_data)

# socket = 'wss://stream.binance.com:9443'
socket = 'wss://stream.binance.com:9443/ws/ethusdt@kline_1m'

ws = websocket.WebSocketApp(socket,on_open=on_open, on_message=on_message)
ws.run_forever()