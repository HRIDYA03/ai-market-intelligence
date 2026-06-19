import requests
from bs4 import BeautifulSoup


class NewsFetcher:

    @staticmethod
    def fetch_google_news(asset):
        """
        Fetch asset-specific news from Google News RSS
        """

        query = asset.replace(".NS", "")

        url = f"https://news.google.com/rss/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"

        news = []

        try:
            response = requests.get(url, timeout=5)
            soup = BeautifulSoup(response.content, "xml")

            articles = soup.find_all("item")

            for a in articles[:10]:
                news.append({
                    "source": "Google",
                    "title": a.title.text
                })

        except Exception as e:
            print("[WARNING] Google news fetch failed")

        return news

    @staticmethod
    def get_all_news(asset):
        return NewsFetcher.fetch_google_news(asset)
