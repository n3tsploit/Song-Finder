from pydub import AudioSegment
from pydub.utils import make_chunks
from base64 import b64encode
import requests
import pprint

myaudio = AudioSegment.from_file("testing.mp3" , "mp3")
chunk_length_ms = 4000 # pydub calculates in millisec
chunks = make_chunks(myaudio, chunk_length_ms) #Make chunks of one sec

frames = []
#Convert chunks to raw audio data which you can then feed to HTTP stream
for i, chunk in enumerate(chunks):
    raw_audio_data = chunk.raw_data
    payload = b64encode(raw_audio_data).decode('utf_8')

    url = "https://shazam.p.rapidapi.com/songs/v2/detect"

    querystring = {"timezone": "America/Chicago", "locale": "en-US"}
    headers = {
        "content-type": "text/plain",
        "X-RapidAPI-Key": "3c1dacced4msh6e95e085f64394ap1ae14fjsn691e92cf4ba5",
        "X-RapidAPI-Host": "shazam.p.rapidapi.com"
    }

    response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

    pprint.pprint(response.text)
    frames.append(raw_audio_data)

frames_data=b''.join(frames)
