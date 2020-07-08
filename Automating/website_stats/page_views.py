from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='/Users/test/Desktop/chromedriver')
driver.get('https://thavasantonio.com')
while True:
    print('view')
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
    driver.get('https://thavasantonio.com/')
    driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 