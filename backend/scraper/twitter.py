import tweepy
from config.settings import TWITTER_API_KEY, TWITTER_API_SECRET

def scrape_twitter():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_SECRET)
    
    api = tweepy.API(auth)

    tweets = api.search_tweets(q="AI", count=10)
    return [{"source": "Twitter", "title": tweet.text, "link": f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"} for tweet in tweets]
