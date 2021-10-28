from selenium import webdriver
import random
import time
import logging
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import os.path
import socket

class Web():
    
    def __init__(self):
        self.driver = self.create_driver()
        self.openSite()
    def create_options(self):
        options = webdriver.ChromeOptions() 
        options.add_argument("start-maximized")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        return options
    def create_driver(self):
        return Chrome(chrome_options=self.create_options(),executable_path='C:/proiect/var_clase/chromedriver.exe')
    def openSite(self,url : str= 'https://www.youtube.com/',title :str = "Youtube"):
        self.driver.maximize_window()
        while self.is_connected()==False:
            try:
                self.driver.get(url)
                WebDriverWait(self.driver, 10).until(EC.title_contains("Youtube"))
                break
            except :
                continue
        self.driver.get(url)
    def is_connected(self):
        try:
            socket.create_connection(("1.1.1.1", 53))
            return True
        except OSError:
            pass
        return False
    
    def acceptCookie(self):
        try:
            css_selector='ytd-button-renderer.ytd-consent-bump-v2-lightbox:nth-child(2) > a:nth-child(1) > tp-yt-paper-button:nth-child(1)'
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))).click()
        except:
            print("no cookie")
    def searchSong(self,search : str='music'):
        while self.is_connected()==False:
            continue
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="search-input"]'))).click()
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="search"]'))).send_keys("music")
        except:
            print("not available")
        while self.is_connected()==False:
            continue        
        for i in range(5):
            try:
                WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="search-icon-legacy"]'))).click()
            except:
                print("can't click search btn")
    def getRandomSong(self):
        while self.is_connected()==False:
            continue    
        for i in range(5):
            try:
                user_data = self.driver.find_elements_by_xpath('//a[@id="thumbnail"]')
            except:
                print("can't find elements")
        print(len(user_data))
        links = []
        for i in user_data:
            links.append(i.get_attribute('href'))
        nr_video=random.randrange(0, len(links))
        while links[nr_video]=="None":
            nr_video=random.randrange(0, len(links))
        self.driver.get(links[nr_video])
    def playSong(self):
        while self.is_connected()==False:
            continue
        xpath_play_btn='/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[5]/button'
        xpath_skip_btn='/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button/div'
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_play_btn))).click()
        except:
            print("can't play video")
        for i in range(3):
            try:
                WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_skip_btn))).click()
            except:
                print("no skip btn")