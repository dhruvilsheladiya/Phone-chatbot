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

# ----- Go To Frontend Folder Then you can change directory like a,
1. cd frontend 
2. run python cli_chatbot.py
3. You:- What's latest phone model?
4. Chatbot reply you:- Final Output!

# I used the same 2025 phone details model, but it got cracked again, so I had to use the old version's phone details models, so it's a chatbot can be response is old details for phone realesing releted details.

🐳 Running with Docker:

docker build -t phone-chatbot .
docker run --env-file .env -it phone-chatbot

🛠 API Testing with Postman:
http://127.0.0.1:8000/chatbot?query=What’s the latest phone model?
# Note:- You should receive a JSON response with the latest phone models.

🎉 Done! Your CLI chatbot is now running inside a Docker container. 🚀


# CREATED BY:- 
#    Dhruvil Sheladiya.



                
