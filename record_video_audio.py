import pyaudio
import wave
import cv2
import numpy as np
import pyautogui
from threading import Thread
import subprocess
import time
import audioop
import math
from scipy.io import wavfile
import scipy.io
import keyboard

def get_db(wav):
    samplerate, data = wavfile.read(wav)
    rms = audioop.rms(data,2)
    lvl_db=20*math.log10( rms )
    f = open("level_of_db.txt", "a")
    f.write("The level of db is: "+str(lvl_db)+'\n')
    f.close()

def record_audio():
    filename = "audio.wav"
    chunk = 1024
    FORMAT = pyaudio.paInt16
    channels = 1
    sample_rate = 44100
    record_seconds = 5
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    while True:
        data = stream.read(chunk)
        frames.append(data)
        if keyboard.is_pressed('q'):
            break
    print("Finished recording.")
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(filename, "wb")
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b"".join(frames))
    wf.close()
    cmd='ffmpeg -y -i video.avi -i audio.wav -map 0:v -map 1:a -c copy output.avi'
    subprocess.call(cmd,shell=True)
    get_db('audio.wav')
    print('Muxing Done')
    

    

def record_video():
    SCREEN_SIZE = (1366, 768)
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("video.avi", fourcc, 20.0, (SCREEN_SIZE))

    while True:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out.write(frame)
        if keyboard.is_pressed('q'):
            break
    cv2.destroyAllWindows()
    out.release()



if __name__=='__main__':
    Thread(target=record_video).start()
    Thread(target=record_audio).start()
 
