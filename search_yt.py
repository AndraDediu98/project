from selenium import webdriver
import random
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_valid_video(links):
	nr_video=random.randrange(0, len(links))
	while links[nr_video]=="None":
		nr_video=random.randrange(0, len(links))
	return links[nr_video]
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(chrome_options=options, executable_path='C:\proiect\chromedriver')
wait = WebDriverWait(driver, 30)
driver.get('https://www.youtube.com/')
css_selector='ytd-button-renderer.ytd-consent-bump-v2-lightbox:nth-child(2) > a:nth-child(1) > tp-yt-paper-button:nth-child(1)'
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))).click() #accept cookie
wait.until(EC.element_to_be_clickable((By.XPATH, '//div[@id="search-input"]'))).click()
wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@id="search"]'))).send_keys("music")
wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@id="search-icon-legacy"]'))).click()
driver.implicitly_wait(20)
user_data = driver.find_elements_by_xpath('//a[@id="thumbnail"]')
links = []
for i in user_data:
    links.append(i.get_attribute('href'))
driver.get(generate_valid_video(links))
driver.implicitly_wait(20)
xpath_play_btn='/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[5]/button'
wait.until(EC.element_to_be_clickable((By.XPATH, xpath_play_btn))).click()
xpath_skip_btn='/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[1]/div/div/div/ytd-player/div/div/div[4]/div/div[3]/div/div[2]/span/button/div'
wait.until(EC.element_to_be_clickable((By.XPATH, xpath_skip_btn))).click()
