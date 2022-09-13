import tweepy
from tweepy import OAuthHandler
from dotenv import load_dotenv
import os

load_dotenv('./.env')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')

client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_secret)

tweets = client.get_home_timeline(max_results=2)

for tweet in tweets.data:
    print(tweet.text)

