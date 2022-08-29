# Import everything needed to edit video clips
from moviepy.editor import *

# loading video dsa gfg intro video
music = AudioFileClip("./songs/yt1s.com - Burna Boy  For My Hand feat Ed Sheeran Official Music Video.mp3")

# clipping of the video
# getting video for only starting 10 seconds
music = music.subclip(0, 10)


music.write_audiofile("teing",fps=44100,nbytes=2,codec="pcm_s16le")