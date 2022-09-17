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

tweets = client.get_home_timeline(media_fields=['preview_image_url'], expansions='attachments.media_keys',
                                     max_results=10)

tweets =list(tweets)

print(tweets)
print('-'*10)
# print(tweets[1]['media'][0].media_key)

for i in range(len(tweets[0])):
    print(tweets[0][i].id)



