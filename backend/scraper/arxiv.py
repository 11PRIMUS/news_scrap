import requests
from bs4 import BeautifulSoup

def scrape_arxiv():
    url = "https://arxiv.org/list/cs.AI/recent"
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    papers = []


    for item in soup.find_all("div", class_="list-title mathjax"):
        title = item.text.strip().replace("Title:", "")
        link = "https://arxiv.org" + item.find_previous("a")["href"]
        
        summary=summarize(title)
        papers.append({"source": "Arxiv", "title": title, "link": link, "summary": summary})
    return papers