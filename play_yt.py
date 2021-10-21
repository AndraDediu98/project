from selenium import webdriver
import pickle
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from subprocess import check_output
from selenium.webdriver.common.by import By
import time, datetime
import sys


random_id=check_output([sys.executable, "random_yt.py"])#get random id for a yt video
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
random_yt_url="https://www.youtube.com/watch?v="+random_id.decode("utf-8") #obtain the url from a random video
driver.implicitly_wait(10)
driver.get(random_yt_url)
css_selector='ytd-button-renderer.ytd-consent-bump-v2-lightbox:nth-child(2) > a:nth-child(1) > tp-yt-paper-button:nth-child(1)'
WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))).click() #accept cookie

#duration = driver.find_elements_by_xpath("//span[@class='ytp-time-duration']")[0].text
#x = time.strptime(duration, '%M:%S')
#x1 = datetime.timedelta(minutes=x.tm_min, seconds=x.tm_sec).total_seconds()







