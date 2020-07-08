from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='/Users/test/Desktop/chromedriver')
driver.get('https://thavasantonio.com')
for i in range(10):
    print('view')
    time.sleep(3)
    driver.refresh()
