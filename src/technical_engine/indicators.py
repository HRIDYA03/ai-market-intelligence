import ta
import pandas as pd

def apply_indicators(df):

    # 🔥 FIX: ensure Close is 1D
    close = df["Close"]

    # If it's 2D, flatten it
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    df["rsi"] = ta.momentum.RSIIndicator(close).rsi()

    return df
