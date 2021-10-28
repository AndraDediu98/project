from threading import Thread
import subprocess
import keyboard

def open_yt():
    cmd='python search_yt.py'
    subprocess.call(cmd,shell=True)

def record():
    while True:
        if keyboard.is_pressed('r'):
            break
    cmd='python record_video_audio.py'
    subprocess.call(cmd,shell=True)

if __name__=='__main__':
    Thread(target=open_yt).start()
    Thread(target=record).start()