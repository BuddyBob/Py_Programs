from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path="/Users/test/Desktop/chromedriver")
driver.get('https://www.y2mate.com/en50')
print("Enter the music url: ")
url = (input())
driver.find_element_by_xpath('//*[@id="txt-url"]').send_keys(url,Keys.ENTER)
time.sleep(2)
mp3 = driver.find_element_by_xpath('//*[@id="result"]/div[1]/div[2]/ul/li[2]/a').click()
time.sleep(2)
down = driver.find_element_by_xpath('//*[@id="process_mp3_a"]').click()
driver.implicitly_wait(10)
download = driver.find_element_by_xpath('//*[@id="dl-btns"]/a').click()
import playsound
playsound.playsound('song.mp3',False)
print ('...')
'''https://www.youtube.com/watch?v=ixkoVwKQaJg'''