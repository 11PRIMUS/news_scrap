import requests
from bs4 import BeautifulSoup
from backend.summarizer import summarize

def scrape_news():
    url = "https://www.artificialintelligence-news.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")

    news = []
    for article in articles[:5]:  # Fetch top 5 articles
        title = article.find("h2").text.strip()
        link = article.find("a")["href"]
        summary = summarize(title)
        news.append({"source": "AI News", "title": title, "link": link, "summary": summary})
    
    return news
