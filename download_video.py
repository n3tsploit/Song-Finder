import tweepy
import json
from dotenv import load_dotenv
import os

load_dotenv('./.env')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')

client = tweepy.Client(consumer_key= consumer_key,consumer_secret= consumer_secret,access_token= access_token,access_token_secret= access_secret)

query = 'covid -is:retweet has:media'

tweets = client.get_home_timeline(tweet_fields=['context_annotations', 'created_at'],
                                     media_fields=['url'], expansions='attachments.media_keys',
                                     max_results=10)

# Get list of media from the includes object
media = {m["media_key"]: m for m in tweets.includes['media']}

for tweet in tweets.data:
    media_keys = tweet['attachments']['media_keys']
    print(tweet)
    if media[media_keys[0]].preview_image_url:
        print(media[media_keys[0]].preview_image_url)


