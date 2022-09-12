import base64
import pprint
import requests
from pydub import AudioSegment

# Crop the audio to ony 5 seconds
sound = AudioSegment.from_mp3("./songs")  # Importing audio file

StrtMin = 0  # start minitute from where you want to crop the audio
StrtSec = 0  # start second from where you want to crop the audio
EndMin = 0  # End minitute of where you want to crop the audio
EndSec = 5  # End second of where you want to crop the audio

StrtTime = StrtMin * 60 * 1000 + StrtSec * 1000  # Convert to milliseconds
EndTime = StrtMin * 60 * 1000 + EndSec * 1000  # Convert to milliseconds

extract = sound[StrtTime:EndTime]  # Croping the audio
extract = extract.set_channels(1)  # make the audio mono

extract.export("./songs/testing.wav", format="wav")  # saving it as a .wav file

# making an Encoded base64 string of byte[] of the audio
with open('./songs/testing.wav', 'rb') as f:
    content = base64.b64encode(f.read())

# sending the request to the api
payload = content
url = "https://shazam.p.rapidapi.com/songs/v2/detect"
querystring = {"timezone": "America/Chicago", "locale": "en-US"}
headers = {
    "content-type": "text/plain",
    "X-RapidAPI-Key": "3c1dacced4msh6e95e085f64394ap1ae14fjsn691e92cf4ba5",
    "X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

pprint.pprint(response.text)
