from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import traceback
driver =  webdriver.Chrome(executable_path='/Users/Aspera/Desktop/chromedriver')
waitshort = WebDriverWait(driver,.5)
wait = WebDriverWait(driver, 20)
waitLonger = WebDriverWait(driver, 10000000000)
visible = EC.visibility_of_element_located
driver.get('https://www.typingclub.com/sportal/program-3.game')

for i in range(100):
    confirm = waitLonger.until(visible((By.XPATH,'//*[@id="root"]/div[2]/div[1]/div[3]/span/div[2]/div[1]/span')))
    try:
        count = 1
        while True:
            otherCount = 0
            lines = wait.until(visible((By.XPATH,'//*[@id="root"]/div[2]/div[5]/div[1]/div/span['+str(count)+']'))).text
            count += 1
            lines = lines.split()
            print(lines)
            for words in lines:
                otherCount += 1
                #Enter
                # if otherCount == len(lines):
                #     inputBox = driver.find_element_by_xpath('/html/body/input').send_keys(words,Keys.ENTER)
                # else:
                inputBox = driver.find_element_by_xpath('/html/body/input').send_keys(words+' ')
                time.sleep(.5)
                
    except Exception as e:
        print(traceback.format_exc())
