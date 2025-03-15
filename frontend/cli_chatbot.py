import requests
import os
from langchain_mistralai import ChatMistralAI

# Load API keys
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "pub_74529d03a4e84c77f78840d7c86f8b40fd150")
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY", "Xat6jS2i2oiO3x6uTFk8gj4RdEvmXjR4")

# Function to fetch latest phone news
def fetch_latest_phone_news():
    url = "https://newsdata.io/api/1/news"
    params = {"apikey": NEWS_API_KEY, "q": "latest phone", "language": "en"}
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        articles = response.json().get("results", [])
        phone_news = [article["title"] for article in articles[:5]]  # Get top 5 articles
        return "\n".join(phone_news) if phone_news else "No recent phone news found."
    else:
        return "Failed to fetch phone news."

# Function to process chatbot response using Mistral AI
def chat_with_ai(user_query):
    mistral_chat = ChatMistralAI(api_key=MISTRAL_API_KEY)
    
    news_data = fetch_latest_phone_news()
    prompt = f"User asked: {user_query}\nLatest Phone Models:\n{news_data}\n\nGenerate a short engaging response."
    
    response = mistral_chat.invoke(prompt)
    return response.content if response else "I couldn't retrieve phone updates right now."

# CLI chatbot
def cli_chatbot():
    print("\n📱 AI Phone News Chatbot - Type 'exit' to quit\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye! 👋")
            break
        response = chat_with_ai(user_input)
        print(f"Chatbot: {response}\n")

if __name__ == "__main__":
    cli_chatbot()
