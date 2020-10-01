from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
level = 2
driver =  webdriver.Chrome(executable_path='/Users/test/Desktop/chromedriver')
waitshort = WebDriverWait(driver,.5)
wait = WebDriverWait(driver, 10)
waitLonger = WebDriverWait(driver, 100)
visible = EC.visibility_of_element_located
driver.get('https://login.mathletics.com/?_ga=2.60361444.876282730.1600105337-1065983887.1599670686&_gac=1.50132436.1600106071.Cj0KCQjwqfz6BRD8ARIsAIXQCf3LZK7GSetOE9YHfbj-cm2Z89tzZRmW-QwIs54eqhKvnkce6x8QB_oaAv_AEALw_wcB')
user = wait.until(visible((By.XPATH,'//*[@id="username"]'))).send_keys('THA10696')
pwd = wait.until(visible((By.XPATH,'//*[@id="password"]'))).send_keys('water73',Keys.ENTER)
play = wait.until(visible((By.XPATH,'//*[@id="student-header"]/div[2]/ul/li[3]/header-button/alert-wrap/div/ng-transclude/div'))).click()
live = wait.until(visible((By.XPATH,'//*[@id="carousel-game-content"]/img'))).click()
level = wait.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/level-selector-directive/div/div['+str(level)+']/button'))).click()
cpu = wait.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[4]/div/div[2]/button'))).click()
go = wait.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[4]/div/go-button/div/button[1]'))).click()
for i in range(31):
    print(i)
    for i in range(89):
        time.sleep(.5)
        txt = waitLonger.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div')))
        question = txt.text
        question = question.split(' ')
        num1 = question[0]
        op = question[1]
        num2 = question[2]
        if op == '+':
            answer = int(num1) + int(num2)
        if op == '-':
            answer = int(num1) - int(num2)
        if op == '×':
            answer = int(num1) * int(num2)
        if op == '÷':
            answer = int(num1) / int(num2)
        try:
            input = wait.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[1]/div[2]/div[2]/aligned-question/div/form/div/input'))).send_keys(answer,Keys.ENTER)
        except: pass
    playagain = waitLonger.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[2]/div[1]/div[2]/play-again-box/div/table[2]/tbody/tr/td[1]/button'))).click()
    # x = wait.until(visible((By.XPATH,'//*[@id="livemathletics"]/body/div[1]/ui-view/div/div[3]/div/div[1]/button'))).click()
    #9:07
    #9:35