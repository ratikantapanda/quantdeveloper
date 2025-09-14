def calculate_capm(ticker):
    import yfinance as yf
    import pandas as pd
    import statsmodels.api as sm

    # Download stock and market data
    stock = yf.download(ticker, start="2020-01-01", end="2025-01-01")['Close']
    market = yf.download("^GSPC", start="2020-01-01", end="2025-01-01")['Close']

    # Compute daily returns
    stock_ret = stock.pct_change().dropna()
    market_ret = market.pct_change().dropna()

    # Align time indexes
    data = pd.concat([stock_ret, market_ret], axis=1)
    data.columns = ["Stock", "Market"]

    # Assume constant risk-free rate (e.g., 4% annual -> daily)
    rf_daily = 0.04 / 252
    data["Stock_excess"] = data["Stock"] - rf_daily
    data["Market_excess"] = data["Market"] - rf_daily

    # Run regression: Stock_excess ~ Market_excess
    X = sm.add_constant(data["Market_excess"])
    y = data["Stock_excess"]
    model = sm.OLS(y, X).fit()

    alpha, beta = model.params

    # Compute expected return using CAPM
    market_premium = data["Market"].mean() * 252 - 0.04  # annualized
    expected_return = 0.04 + beta * market_premium

    return {
        "alpha": alpha,
        "beta": beta,
        "expected_return": expected_return
    }