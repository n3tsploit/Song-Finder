import base64
import pprint
import requests
from pydub import AudioSegment
from moviepy.editor import *

# extracting the audio from the video
video_clip = VideoFileClip('./songs/yt1s.com - Bien x Aaron Rimbui  Mbwe Mbwe Official Music Video_v240P.mp4')
audio_clip = video_clip.audio
audio_clip.write_audiofile('./songs/testing.mp3')
audio_clip.close()
video_clip.close()

# Crop the audio to ony 5 seconds
sound = AudioSegment.from_mp3("./songs/testing.mp3")  # Importing audio file

start_min = 0  # start minitute from where you want to crop the audio
start_sec = 0  # start second from where you want to crop the audio
end_min = 0  # End minitute of where you want to crop the audio
end_sec = 5  # End second of where you want to crop the audio

start_time = start_min * 60 * 1000 + start_sec * 1000  # Convert to milliseconds
end_time = start_min * 60 * 1000 + end_sec * 1000  # Convert to milliseconds

extract = sound[start_time:end_time]  # Croping the audio
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
    "X-RapidAPI-Key": "key",
    "X-RapidAPI-Host": "shazam.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

pprint.pprint(response.text)
