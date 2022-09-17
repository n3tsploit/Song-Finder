import pprint
import time

import tweepy
import json
from dotenv import load_dotenv
import os

load_dotenv('./.env')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')

client = tweepy.Client(bearer_token=bearer_token)

query = 'bsides nairobi has:media'


response = client.search_recent_tweets(query=query,tweet_fields=['created_at','lang'], expansions=['author_id'], user_fields=['profile_image_url'], media_fields=['url','type'])
users = {u['id']:u for u in response.includes['users']}

pprint.pprint(response)

for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(tweet.id)
        print(user.type)
