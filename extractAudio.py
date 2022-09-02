from pydub import AudioSegment
import base64
import pprint
import requests

#importing file from location by giving its path
sound = AudioSegment.from_mp3("./songs/yt1s.com - Burna Boy  For My Hand feat Ed Sheeran Official Music Video.mp3")

#Selecting Portion we want to cut
StrtMin = 0
StrtSec = 10

EndMin = 0
EndSec = 15

# Time to milliseconds conversion
StrtTime = StrtMin*60*1000+StrtSec*1000
EndTime = StrtMin*60*1000+EndSec*1000

# Opening file and extracting portion of it
extract = sound[StrtTime:EndTime]

# Saving file in required location
extract.export("./testing.mp3", format="mp3")

# new file portion.mp3 is saved at required location

raw_audio = AudioSegment.from_file("testing.mp3", format="mp3",
                                   frame_rate=44100, channels=1, sample_width=2)

raw_audio.export("testing.mp3", format="mp3")

#jjjj

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
