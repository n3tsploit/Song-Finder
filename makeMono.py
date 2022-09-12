from pydub import AudioSegment
sound = AudioSegment.from_mp3("./testing.wav")
sound = sound.set_channels(1)
sound.export("./new.wav", format="wav")