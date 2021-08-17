from selenium import *
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path='/Users/test/Desktop/chromedriver')
driver.get('https://filebin.net')
driver.find_element_by_xpath('//*[@id="fileField"]').send_keys('file path')