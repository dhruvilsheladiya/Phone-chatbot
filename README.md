# Phone Chatbot (CLI) - Mistral AI & News API

This is a CLI-based chatbot that fetches the latest phone models using a news API and provides AI-powered responses using Mistral AI.

## 🚀 Features
- Uses **Mistral AI** for natural language processing.
- Fetches **latest phone news** via `NewsData.io` API.
- Runs as a **Docker container** for easy deployment.

## 📂 Project Structure
phone-chatbot/ │── backend/ │ ├── main.py # CLI Chatbot Runner │ ├── ai_chat.py # AI Processing (Mistral API) │ ├── news_fetcher.py # Fetches latest phone news │── Dockerfile │── requirements.txt │── .env │── README.md

phone-chatbot/ │── backend/ │ ├── cli_chatbot.py |--- requirments.txt

## How To Run:- 
1. pip install -r requirements.txt
2. .env file =
 NEWS_API_KEY=your_news_api_key
 MISTRAL_API_KEY=your_mistral_api_key
3. python backend/main.py

🐳 Running with Docker:

docker build -t phone-chatbot .
docker run --env-file .env -it phone-chatbot

🛠 API Testing with Postman:
http://127.0.0.1:8000/chatbot?query=What’s the latest phone model?
# Note:- You should receive a JSON response with the latest phone models.

🎉 Done! Your CLI chatbot is now running inside a Docker container. 🚀


# CREATED BY:- 
#    Dhruvil Sheladiya.



                
