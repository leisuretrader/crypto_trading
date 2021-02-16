import websocket

def on_open(ws):
    print ('the socket is open')

def on_message(ws, message):
    print (message)

socket = "wss://stream.binance.com:9443/ws/btcusdt@trade"

ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()