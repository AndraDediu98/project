from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from subprocess import check_output
import random
from selenium.webdriver.common.by import By
import time, datetime
import sys
import cv2
import numpy as np
import pyautogui
from threading import Thread

def generate_valid_video(links):
	nr_video=random.randrange(0, len(links))
	while links[nr_video]=="None":
		nr_video=random.randrange(0, len(links))
	return links[nr_video]

def play_random_yt_video():
	driver = webdriver.Chrome('./chromedriver')
	driver.maximize_window()
	wait = WebDriverWait(driver, 30)
	driver.get('https://www.youtube.com/')
	css_selector='ytd-button-renderer.ytd-consent-bump-v2-lightbox:nth-child(2) > a:nth-child(1) > tp-yt-paper-button:nth-child(1)'
	wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))).click() #accept cookie
	wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="search-icon-legacy"]')))
	searchbox = driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div[1]/div[1]/input')
	searchbox.send_keys("music")
	searchbutton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]') 
	searchbutton.click()
	driver.implicitly_wait(10)
	user_data = driver.find_elements_by_xpath('//a[@id="thumbnail"]')
	links = []
	for i in user_data:
		links.append(i.get_attribute('href'))
	driver.get(generate_valid_video(links))
	driver.implicitly_wait(10)
	xpath_play_btn='/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[5]/button'
	wait.until(EC.element_to_be_clickable((By.XPATH, xpath_play_btn))).click()


def record_video():
	SCREEN_SIZE = (1360, 768)
	# define the codec
	fourcc = cv2.VideoWriter_fourcc(*"XVID")
	# create the video write object
	out = cv2.VideoWriter("output.avi", fourcc, 24.0, (SCREEN_SIZE))
	for i in range(240):
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


