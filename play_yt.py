from selenium import webdriver
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from subprocess import check_output
import sys

random_id=check_output([sys.executable, "random_yt.py"])
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
driver.maximize_window()
random_yt_url="https://www.youtube.com/watch?v="+random_id.decode("utf-8") 
driver.get(random_yt_url)




