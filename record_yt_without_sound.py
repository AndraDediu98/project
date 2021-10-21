from selenium import webdriver
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from subprocess import check_output
from selenium.webdriver.common.by import By
import time, datetime
import sys
import cv2
import numpy as np
import pyautogui
from threading import Thread

def play_random_yt_video():
	random_id=check_output([sys.executable, "random_yt.py"])#get random id for a yt video
	driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
	driver.maximize_window()
	random_yt_url="https://www.youtube.com/watch?v="+random_id.decode("utf-8") #obtain the url from a random video
	driver.implicitly_wait(10)
	driver.get(random_yt_url)
	css_selector='ytd-button-renderer.ytd-consent-bump-v2-lightbox:nth-child(2) > a:nth-child(1) > tp-yt-paper-button:nth-child(1)'
	WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))).click() #accept cookie

def record_video():
	SCREEN_SIZE = (1360, 768)
	# define the codec
	fourcc = cv2.VideoWriter_fourcc(*"XVID")
	# create the video write object
	out = cv2.VideoWriter("output.avi", fourcc, 10.0, (SCREEN_SIZE))
	for i in range(400):
	    # make a screenshot
	    img = pyautogui.screenshot()
	    # convert these pixels to a proper numpy array to work with OpenCV
	    frame = np.array(img)
	    # convert colors from BGR to RGB
	    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	    # write the frame
	    out.write(frame)
	out.release()
if __name__=='__main__':
	Thread(target=play_random_yt_video).start()
	Thread(target=record_video).start()


