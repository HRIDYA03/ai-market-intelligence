from src.data_engine.market_data import fetch_data
from src.technical_engine.indicators import apply_indicators


asset = input("Enter asset: ")

df = fetch_data(asset)

df = df.dropna()

if df.empty:
    print("No data found")
else:
    df = apply_indicators(df)
    print(df.tail())
