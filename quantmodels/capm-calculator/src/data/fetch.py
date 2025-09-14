import yfinance as yf
import pandas as pd

def fetch_data(tickers, start_date, end_date):
    stock_data = {}
    for ticker in tickers:
        stock_data[ticker] = yf.download(ticker, start=start_date, end=end_date)['Close']
    market_data = yf.download("^GSPC", start=start_date, end=end_date)['Close']
    return stock_data, market_data