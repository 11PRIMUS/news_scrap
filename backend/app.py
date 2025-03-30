from fastapi import FastAPI
from backend.db.database import get_db, init_db
from backend.scraper.ai_news_scraper import scrape_news
from backend.summarizer import summarize

app = FastAPI()

@app.get("/")
def home():
    return {"message": "launch tracker running"}

@app.get("/scrape/")
def fetch_ai_news():
    news = scrape_news()
    summarized_news = [summarize(n["content"]) for n in news]
    return summarized_news