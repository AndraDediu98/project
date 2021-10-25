from selenium import webdriver
import random
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Chrome, ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

class Web():
    
    def __init__(self):
        self.driver = self.create_driver()
        self.openSite()
    def create_driver(self):
        return Chrome(ChromeDriverManager().install())
    def openSite(self,url : str= 'https://www.youtube.com/'):
        self.driver.maximize_window()
        self.driver.get(url)
    def acceptCookie(self):
        css_selector='ytd-button-renderer.ytd-consent-bump-v2-lightbox:nth-child(2) > a:nth-child(1) > tp-yt-paper-button:nth-child(1)'
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))).click()
    def searchSong(self,search : str='music'):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id="search-input"]'))).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//input[@id="search"]'))).send_keys("music")
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[@id="search-icon-legacy"]'))).click()
    def getRandomSong(self):
        user_data = self.driver.find_elements_by_xpath('//a[@id="thumbnail"]')
        links = []
        for i in user_data:
            links.append(i.get_attribute('href'))
        nr_video=random.randrange(0, len(links))
        while links[nr_video]=="None":
            nr_video=random.randrange(0, len(links))
        self.driver.get(links[nr_video])
    def playSong(self):
        xpath_play_btn='/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[5]/button'
        xpath_skip_btn='/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button/div'
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_play_btn))).click()
        except:
            print("can't play video")
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_skip_btn))).click()
        except:
            print("no skip btn")