import yfinance as yf
import pandas as pd


def fetch_data(asset):
    df = yf.download(asset, period="3mo", interval="1d", progress=False)

    # Fix multi-index columns (important)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    return df
