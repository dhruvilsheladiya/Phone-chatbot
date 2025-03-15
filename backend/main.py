from fastapi import FastAPI
import requests
import re

app = FastAPI()

NEWS_API_URL = "https://newsdata.io/api/1/news"
NEWS_API_KEY = "pub_74529d03a4e84c77f78840d7c86f8b40fd150"

# Define keywords to filter relevant news
PHONE_KEYWORDS = ["Samsung", "iPhone", "OnePlus", "Xiaomi", "Pixel", "Motorola", "Oppo", "Vivo", "Asus", "Nokia", "Huawei"]

def extract_phone_models(articles):
    """Filter and extract only relevant phone model news."""
    phone_news = []
    
    for article in articles:
        title = article.get("title", "")
        
        # Check if the title contains any smartphone-related brand name
        if any(keyword in title for keyword in PHONE_KEYWORDS):
            phone_news.append(title)
    
    return phone_news[:5]  # Return only top 5 relevant news

@app.get("/chatbot")
def chatbot_query(query: str):
    """Process user query and return latest phone model news."""
    if "latest phone" in query.lower():
        response = requests.get(f"{NEWS_API_URL}?apikey={NEWS_API_KEY}&q=smartphone")
        
        if response.status_code == 200:
            news_data = response.json()
            articles = news_data.get("results", [])

            # Filter out only relevant phone model news
            latest_phones = extract_phone_models(articles)

            if not latest_phones:
                return {"response": "I couldn't find any latest phone model news right now. Try again later!"}

            return {"response": f"Here are the latest phone models:\n" + "\n".join(latest_phones)}

    return {"response": "I'm not sure about that. Can you ask differently?"}
