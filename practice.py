import requests
import pyaudio
from base64 import b64encode

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 4

audio = pyaudio.PyAudio()

# start Recording
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
print("recording...")
frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
print("finished recording")

# stop Recording
stream.stop_stream()
stream.close()
audio.terminate()

frames_data = b''.join(frames)
payload = b64encode(frames_data).decode('utf_8')

url = "https://shazam.p.rapidapi.com/songs/detect"

headers = {
    "content-type": "text/plain",
    "X-RapidAPI-Key": "3c1dacced4msh6e95e085f64394ap1ae14fjsn691e92cf4ba5",
    "X-RapidAPI-Host": "shazam.p.rapidapi.com"
}
querystring = {"timezone": "America/Chicago", "locale": "en-US"}
response = requests.request("POST", url, data=payload, headers=headers, params=querystring)

print(response.text)