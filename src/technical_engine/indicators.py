import ta
import pandas as pd


def apply_indicators(df):

    close = df["Close"]

    # Ensure 1D data
    if isinstance(close, pd.DataFrame):
        close = close.iloc[:, 0]

    df["rsi"] = ta.momentum.RSIIndicator(close).rsi()

    return df
