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

query = 'usiu has:media'


response = client.search_recent_tweets(query=query,tweet_fields=['created_at','lang'], expansions=['attachments.media_keys','author_id'], user_fields=['profile_image_url'])
users = {u['id']:u for u in response.includes['users']}
medias = {m['media_key']:m for m in response.includes['media']}

# pprint.pprint(medias)
# pprint.pprint(response)

for tweet in response.data:
    if users[tweet.author_id]:
        user = users[tweet.author_id]
        print(tweet.id)
        print(user.username)

# for tweet in response.data:
#     try:
#         if medias[tweet.attachments['media_keys'][0]]:
#             mediam = medias[tweet.attachments['media_keys'][0]]
#             print(mediam.media_key)
#     except:
#         pass