from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/Users/test/Desktop/chromedriver")
driver.get('https://www.mcrpg.com/kohi-click-test/')
while True:
    try:
        driver.find_element_by_xpath('//*[@id="vue"]/button').click()
    except Exception:
        time.sleep(10)