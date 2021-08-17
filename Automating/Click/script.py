from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
driver =  webdriver.Chrome(executable_path='/Users/Aspera/Desktop/chromedriver')
wait = WebDriverWait(driver, .0000000000000000000000000000000000000000000000000000000000000000001)
waitnorm = WebDriverWait(driver, 1000000000000000000)
visible = EC.visibility_of_element_located
driver.get('http://cpstest.org')
driver.execute_script("window.scrollTo(0, 500)") 
level = waitnorm.until(visible((By.XPATH,'//*[@id="wrapper"]/div[3]/div/div[2]/div[2]/div/div[2]/button[1]'))).click()
try:
    start = waitnorm.until(visible((By.XPATH,'//*[@id="start"]'))).click()
except:
    pass
while True:
    try:
        button = wait.until(visible((By.XPATH,'//*[@id="clickarea"]'))).click()
    except:
        pass


    


