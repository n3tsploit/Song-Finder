import base64
import pprint
import moviepy
import requests

url = "https://shazam.p.rapidapi.com/songs/v2/detect"

querystring = {"timezone": "America/Chicago", "locale": "en-US"}

with open('./testing.raw', 'rb') as f:
    content = base64.b64encode(f.read())
payload = content
headers = {
    "content-type": "text/plain",
    "X-RapidAPI-Key": "3c1dacced4msh6e95e085f64394ap1ae14fjsn691e92cf4ba5",
    "X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

pprint.pprint(response.text)

# how to change audio files to raw in python
