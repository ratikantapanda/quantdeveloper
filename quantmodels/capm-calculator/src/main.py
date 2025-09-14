import yfinance as yf
import pandas as pd
from capm import calculate_capm

def main():
    tickers = input("Enter company tickers separated by commas: ").split(',')
    tickers = [ticker.strip() for ticker in tickers]
    
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")
    
    for ticker in tickers:
        alpha, beta, expected_return = calculate_capm(ticker, start_date, end_date)
        print(f"{ticker}: Alpha = {alpha:.6f}, Beta = {beta:.4f}, Expected Return = {expected_return:.2%}")

if __name__ == "__main__":
    main()