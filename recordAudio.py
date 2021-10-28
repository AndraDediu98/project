import pyaudio
import wave
import keyboard
from threading import Thread

class RecordAudio():
    def __init__(self,filename : str = "audio.wav" ):
        self.filename = filename
        self.chunk = 1024
        self.FORMAT = pyaudio.paInt16
        self.channels = 1
        self.sample_rate = 44100
    def record(self,duration : int =120):
        p = pyaudio.PyAudio()
        stream = p.open(format=self.FORMAT,
                        channels=self.channels,
                        rate=self.sample_rate,
                        input=True,
                        output=True,
                        frames_per_buffer=self.chunk)
        frames = []
        print("Recording...")
        for i in range(int(44100 / self.chunk * duration)):
            data = stream.read(self.chunk)
            frames.append(data)
            if keyboard.is_pressed('q'):
                break
        print("Finished recording.")
        stream.stop_stream()
        stream.close()
        p.terminate()
        wf = wave.open(self.filename, "wb")
        wf.setnchannels(self.channels)
        wf.setsampwidth(p.get_sample_size(self.FORMAT))
        wf.setframerate(self.sample_rate)
        wf.writeframes(b"".join(frames))
        wf.close()
    def joinThread(self):
        return Thread(target=self.record)