# market_data_publisher.py
import zmq, random, time

ctx = zmq.Context()
pub = ctx.socket(zmq.PUB)
pub.bind("tcp://*:6000")

symbols = ["AAPL", "MSFT", "SPY"]

while True:
    sym = random.choice(symbols)
    price = round(100 + random.random() * 10, 2)
    pub.send_multipart([sym.encode(), str(price).encode()])
    time.sleep(0.01)  # simulate tick
