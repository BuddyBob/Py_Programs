#import modules
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver =  webdriver.Chrome(executable_path='/Users/aspera/Desktop/chromedriver')
waitshort = WebDriverWait(driver,.5)
wait = WebDriverWait(driver, 20)
waitLonger = WebDriverWait(driver, 100)
visible = EC.visibility_of_element_located
driver.get('https://play2048.co')

grid= wait.until(visible((By.CSS_SELECTOR, "body")))
direction = [Keys.RIGHT, Keys.DOWN, Keys.LEFT]
count = 0
scores=[]
while True:
    count += 1
    grid.send_keys(random.choice(direction))
    try:
        startOver=driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[1]/div/a[2]').click()
    except:
        pass