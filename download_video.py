import pprint
import time
import requests
import tweepy
import json
from dotenv import load_dotenv
import os
# import wget

load_dotenv('./.env')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')


response = requests.get(url='https://api.twitter.com/2/tweets?ids=1571483067461603330&expansions=attachments.media_keys&media.fields=type,variants', headers={'Authorization': f'Bearer {bearer_token}'})
data = response.json()

print(data['includes']['media'][0]['variants'][0]['url'])