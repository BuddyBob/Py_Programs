
def racing():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import NoSuchElementException
    import time
    driver =  webdriver.Chrome(executable_path='/Users/Aspera/Desktop/chromedriver')
    waitshort = WebDriverWait(driver,.5)
    wait = WebDriverWait(driver, 20)
    waitLonger = WebDriverWait(driver, 100000)
    visible = EC.visibility_of_element_located
    driver.get('https://www.nitrotype.com/?utm_source=typing&utm_medium=referral&utm_campaign=crosspromo&utm_content=games')

    login = wait.until(visible((By.XPATH,'//*[@id="root"]/div/header/div/div[2]/div[3]/div/div[1]/a'))).click()
    username = wait.until(visible((By.XPATH,'//*[@id="username"]'))).send_keys('dumbas1')
    pwd = wait.until(visible((By.XPATH,'//*[@id="password"]'))).send_keys('Coollunch59',Keys.ENTER)
    race = wait.until(visible((By.XPATH,'//*[@id="root"]/div/header/div/div[3]/div[1]/a'))).click()

    for i in range(2):

        waitThing = waitLonger.until(visible((By.XPATH,'//*[@id="raceContainer"]/div[4]/div[1]/div[1]/div[2]/div[1]')))
        try:
            for i in range(1,100):  
                container=  wait.until(visible((By.XPATH,'//*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]'))).text
                print(container)

                word = wait.until(visible((By.XPATH,'//*[@id="raceContainer"]/div[3]/div[1]/div[1]/div[2]/div[1]/div/span['+str(i)+']'))).text
                print(word)
                
                element = driver.find_element_by_class_name('dash-copy-input').send_keys(word)
                print('done')
                
                time.sleep(.2)
        except:
            pass


racing()





