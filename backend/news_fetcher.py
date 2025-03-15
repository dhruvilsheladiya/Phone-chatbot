import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API key and URL
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_URL = "https://newsdata.io/api/1/news"

def fetch_latest_news():
    """Fetch latest phone-related news articles."""
    params = {"apikey": NEWS_API_KEY, "q": "latest phone"}
    response = requests.get(NEWS_API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        articles = data.get("results", [])
        latest_models = [article["title"] for article in articles[:5]]
        return "\n".join(latest_models) if latest_models else "No latest phone models found."
    
    return "Failed to fetch news."

if __name__ == "__main__":
    print(fetch_latest_news())
