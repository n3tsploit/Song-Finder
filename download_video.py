import pprint
import time
import requests
import tweepy
import json
from dotenv import load_dotenv
import os
import wget

load_dotenv('./.env')
consumer_key = os.getenv('CONSUMER_KEY')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_KEY')
access_secret = os.getenv('ACCESS_SECRET')
bearer_token = os.getenv('BEARER_TOKEN')
user_id = os.getenv('USER_ID')

response = requests.get(url=f'https://api.twitter.com/2/users/{user_id}/mentions?expansions=attachments.media_keys&media.fields=type,variants', headers={'Authorization': f'Bearer {bearer_token}'})
id = response.json()['data'][0]['id']

response1 = requests.get(url=f'https://api.twitter.com/2/tweets?ids={id}&expansions=attachments.media_keys&media.fields=type,variants', headers={'Authorization': f'Bearer {bearer_token}'})
data = response1.json()
# url = data['includes']['media'][0]['variants'][0]['url']

print(data)
# file = wget.download(url)