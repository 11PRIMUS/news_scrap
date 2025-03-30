from fastapi import FastAPI
from backend.scraper.news import scrape_news
from backend.summarizer import summarize
from backend.db.database import init_db

app = FastAPI()

@app.on_event("startup")
async def startup():
    init_db()

@app.get("/")
def home():
    return {"message": "launch tracker running"}

@app.get("/scrape/")
def fetch_ai_news():
    news = scrape_news()
    summarized_news = [summarize(n["content"]) for n in news]
    return summarized_news
