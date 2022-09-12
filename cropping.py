from pydub import AudioSegment
import base64
import pprint
import requests

#importing file from location by giving its path
sound = AudioSegment.from_mp3("./songs/yt1s.com - Burna Boy  For My Hand feat Ed Sheeran Official Music Video.mp3")

#Selecting Portion we want to cut
StrtMin = 0
StrtSec = 0

EndMin = 0
EndSec = 5

# Time to milliseconds conversion
StrtTime = StrtMin*60*1000+StrtSec*1000
EndTime = StrtMin*60*1000+EndSec*1000

# Opening file and extracting portion of it
extract = sound[StrtTime:EndTime]

# Saving file in required location
extract.export("./testing.wav", format="wav")

