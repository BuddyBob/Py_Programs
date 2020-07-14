from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='/Users/test/Desktop/chromedriver')
driver.get('https://www.123test.com/personality-test/')
count = 1
for i in range(20):
    btn = driver.find_element_by_id('its123-item-PERSONALITY_US_00'+str(count)+'-5').click()
    count+=1
    time.sleep(2)