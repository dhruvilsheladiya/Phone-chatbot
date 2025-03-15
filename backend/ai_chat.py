import os
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain.schema import HumanMessage
from langchain_huggingface import HuggingFaceEmbeddings
import faiss
import numpy as np

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Load AI model
llm = ChatMistralAI(mistral_api_key=MISTRAL_API_KEY)

# Load HuggingFace embeddings
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# FAISS Vector Store
news_data = []  # Store news articles
news_vectors = None  # Store embeddings

def process_news(news_articles):
    """Embed news articles and store in FAISS"""
    global news_data, news_vectors

    texts = [article["title"] for article in news_articles]
    embeddings = embedding_model.embed_documents(texts)

    if len(embeddings) > 0:
        dim = len(embeddings[0])
        news_vectors = faiss.IndexFlatL2(dim)
        news_vectors.add(np.array(embeddings))
        news_data = news_articles

def get_relevant_news(query):
    """Retrieve most relevant news based on query"""
    if news_vectors is None or len(news_data) == 0:
        return "No news data available."

    query_embedding = np.array(embedding_model.embed_query(query)).reshape(1, -1)
    _, indices = news_vectors.search(query_embedding, 1)

    index = indices[0][0]
    return news_data[index]["title"] + " - " + news_data[index]["link"]

def chat_with_ai(query):
    """Generate chatbot response"""
    relevant_news = get_relevant_news(query)
    
    prompt = f"""
    User Query: {query}
    Latest Phone News: {relevant_news}
    
    Respond in a friendly and engaging way.
    """

    response = llm.invoke(prompt)
    return response.content
