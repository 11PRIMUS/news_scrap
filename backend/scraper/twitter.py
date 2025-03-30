import tweepy
from backend.summarizer import summarize
from backend.config.settings import TWITTER_API_KEY, TWITTER_API_SECRET

auth = tweepy.AppAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
api = tweepy.API(auth)

def scrape_twitter():
    tweets = api.search_tweets(q="AI Launch", count=5, lang="en")
    return [{"source": "Twitter", "title": tweet.text, "link": f"https://twitter.com/user/status/{tweet.id}", "summary": summarize(tweet.text)} for tweet in tweets]
