import requests
import pyaudio
from base64 import b64encode

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 4
WAVE_OUTPUT_FILENAME = "file.wav"

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
    'x-rapidapi-host': "shazam.p.rapidapi.com",
    'x-rapidapi-key': "MY-KEY",
    'content-type': "text/plain",
    'accept': "text/plain"
}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
