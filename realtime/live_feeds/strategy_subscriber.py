# strategy_subscriber.py
import zmq

ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect("tcp://localhost:6000")
sub.setsockopt_string(zmq.SUBSCRIBE, "AAPL")  # filter by symbol

while True:
    sym, price = sub.recv_multipart()
    print(f"{sym.decode()} price={float(price)}")
