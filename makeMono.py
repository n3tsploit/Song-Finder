from pydub import AudioSegment
sound = AudioSegment.from_mp3("./testing.mp3")
sound = sound.set_channels(1)
sound.export("./new.raw", format="paInt16")