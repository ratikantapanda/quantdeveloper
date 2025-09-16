# task_dispatcher.py
import zmq

ctx = zmq.Context()
push = ctx.socket(zmq.PUSH)
push.bind("tcp://*:6001")

symbols = ["AAPL", "MSFT", "GOOG", "SPY"]
for sym in symbols:
    push.send_string(sym)
