from src.data_engine.market_data import fetch_data
from src.technical_engine.indicators import apply_indicators
from src.data_engine.news_fetcher import NewsFetcher


def run():

    asset = input("Enter asset: ")

    # ======================
    # MARKET DATA
    # ======================
    df = fetch_data(asset)

    if df.empty:
        print("No data found")
        return

    df = apply_indicators(df)
    df = df.dropna()

    print("\n===== MARKET DATA =====")
    print(df.tail())

    # ======================
    # NEWS
    # ======================
    print("\n===== NEWS =====")

    news = NewsFetcher.get_all_news(asset)

    for i, article in enumerate(news, 1):
        print(f"{i}. [{article['source']}] {article['title']}")


if __name__ == "__main__":
    run()
