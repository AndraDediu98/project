import cv2
import numpy as np
import pyautogui
import keyboard
from threading import Thread

class RecordVideo():
    def __init__(self,filename : str ="video.avi"):
        self.screenSize=(1366, 768)
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.filename=filename
        self.out = cv2.VideoWriter(self.filename, self.fourcc, 16.0, self.screenSize)
    def record(self, duration : int =120):
        print("start recording")
        for i in range(15 * duration):
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)
            if keyboard.is_pressed('q'):
                break
        print("finish video recording")
        cv2.destroyAllWindows()
        self.out.release()
    def joinThread(self):
        return Thread(target=self.record)