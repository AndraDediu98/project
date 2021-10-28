from WebScraping import Web
from record_video import RecordVideo
from recordAudio import RecordAudio
from threading import Thread
import subprocess
import time
import audioop
import math
from scipy.io import wavfile
import scipy.io
import wave
import time
import keyboard

def get_db(wav):
    samplerate, data = wavfile.read(wav)
    rms = audioop.rms(data,2)
    lvl_db=20*math.log10( rms )
    f = open("level_of_db.txt", "a")
    f.write("The level of db is: "+str(lvl_db)+'\n')
    f.close()

def navigateWeb():
    web=Web()
    web.acceptCookie()
    web.searchSong()
    web.getRandomSong()
    web.playSong()
    while True:
        if keyboard.is_pressed('s'):
            break
def recordAudioVideo():
    audio=RecordAudio()
    video=RecordVideo()
    while True:
        if keyboard.is_pressed('r'):
            break
    task1=audio.joinThread()
    task2=video.joinThread()
    task2.start()
    task1.start()
    task1.join()
    task2.join()
    while task1.is_alive() and  task2.is_alive():
        continue
    subprocess.run(["C:/proiect/ffmpeg","-y", "-i", video.filename, "-i", audio.filename, "-map", "0:v", "-map", "1:a", "-c", "copy", "out.avi"],creationflags=subprocess.CREATE_NO_WINDOW)
    get_db('audio.wav')
    print('Muxing Done')
    


if __name__ == '__main__':
    task1=Thread(target=navigateWeb)
    task2=Thread(target=recordAudioVideo)
    task1.start()
    task2.start()
    task1.join()
    task2.join()
