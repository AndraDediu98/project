import cv2
import numpy as np
import pyautogui
import keyboard
from threading import Thread

class RecordVideo():
    def setUp(self,filename : str ="video.avi"):
        self.screenSize=(1366, 768)
        self.fourcc = cv2.VideoWriter_fourcc(*"XVID")
        self.filename=filename
        self.out = cv2.VideoWriter(self.filename, self.fourcc, 20.0, self.screenSize)
    def record(self):
        while True:
            img = pyautogui.screenshot()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.out.write(frame)
            if keyboard.is_pressed('q'):
                break
        cv2.destroyAllWindows()
        self.out.release()
    def joinThread(self):
        return Thread(target=self.record)