import requests
from bs4 import BeautifulSoup

def scrape_github():
    url = "https://github.com/trending/ai?since=daily"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    repos = []
    for repo in soup.find_all("h2", class_="h3 lh-condensed"):
        title = repo.text.strip()
        link = "https://github.com" + repo.a["href"]
        repos.append({"source": "GitHub", "title": title, "link": link})
    return repos