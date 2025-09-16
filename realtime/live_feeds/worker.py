# worker.py
import zmq

ctx = zmq.Context()
pull = ctx.socket(zmq.PULL)
pull.connect("tcp://localhost:6001")

while True:
    sym = pull.recv_string()
    # Run heavy backtest or factor calc
    print(f"Backtesting {sym}")
