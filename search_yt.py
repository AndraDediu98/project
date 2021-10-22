from selenium import webdriver
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def generate_valid_video(links):
	nr_video=random.randrange(0, len(links))
	while links[nr_video]=="None":
		nr_video=random.randrange(0, len(links))
	return links[nr_video]

driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()
wait = WebDriverWait(driver, 30)
driver.get('https://www.youtube.com/')
css_selector='ytd-button-renderer.ytd-consent-bump-v2-lightbox:nth-child(2) > a:nth-child(1) > tp-yt-paper-button:nth-child(1)'
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))).click() #accept cookie
driver.implicitly_wait(10)
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


