def compute_returns(data):
    return data.pct_change().dropna()

def align_data(stock_ret, market_ret):
    return pd.concat([stock_ret, market_ret], axis=1).dropna()