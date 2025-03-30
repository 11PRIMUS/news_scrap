import requests

def scrape_reddit():
    url = "https://www.reddit.com/r/artificial/new.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        posts = response.json()["data"]["children"]

        return [{"source": "Reddit", "title": post["data"]["title"], "link": post["data"]["url"]} for post in posts]
    return []