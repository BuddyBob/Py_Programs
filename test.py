from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# Python3 code to demonstrate 
# generating random strings  
# using random.choices() 
import string 
import random 
# initializing size of string  
N = 7
  
# using random.choices() 
# generating random strings  
res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = N)) 
  
substring = "fitschool.be"

options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

driver=webdriver.Chrome(options='/Users/test/Desktop/chromedriver')
driver.get("https://www.wattpad.com/login")
signup=driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div/div[2]/main/div/div/div/footer/span/button")
signup.click()
button=driver.find_element_by_xpath ("/html/body/div[3]/div/div[3]/div/div[2]/main/div/div/div/div/div/button")
button.click()
username=driver.find_element_by_id ("signup-username")
username.send_keys(str(res))


second_tab = webdriver.Chrome(options=options,)

second_tab.get("https://www.tempinbox.xyz/")
randombutton = second_tab.find_element_by_xpath("/html/body/main/div[1]/div/div[1]/div[2]/form[1]/input[2]") #for the email generation
randombutton.send_keys(str(res))
mainurl = second_tab.current_url

selectoption1=second_tab.find_element_by_xpath("//div[@id='selected-domain']").click()
selectoption2=second_tab.find_element_by_xpath("//a[contains(text(),'@fitschool.be')]").click()

clickfinal= second_tab.find_element_by_xpath("//input[@value='Create']").click()
emailentry = str(res)+ "@fitschool.be"

print ("your email is " + emailentry)

emailspace = driver.find_element_by_id ("signup-email")
emailspace.send_keys(emailentry)
password = driver.find_element_by_id ("signup-password")
password.send_keys ("subscribe")
driver.find_element_by_xpath("//select[@id='signup-month']/option[text()='Nov']").click()
driver.find_element_by_xpath("//select[@id='signup-day']/option[text()='18']").click()
driver.find_element_by_xpath("//select[@id='signup-year']/option[text()='1996']").click()
submitbutton=driver.find_element_by_xpath("//input[@value='Sign up with email']").click()
print("acount maker done")

with open(r"C:\Users\BRS\Desktop\wattpad.txt", 'a',encoding = "utf-8") as outfile:
    outfile.write(emailentry)

outfile.close()    

time.sleep(10)




WebDriverWait(second_tab, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='mails']//div[@class='message']"))).click()
linky= second_tab.find_element_by_xpath("//a[contains(text(),'This is me!')]").get_attribute('href')
second_tab.get(linky)





'''verilink= input("enter the verification link:\n")
driver.get(verilink)'''
time.sleep(5)
driver.get("https://www.wattpad.com/893851831-my-2nd-year-chapter-1")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()

driver.get("https://www.wattpad.com/893856960-my-2nd-year-chapter-2-10-minutes-later")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()


driver.get("https://www.wattpad.com/894447654-my-2nd-year-chapter-3")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()


driver.get("https://www.wattpad.com/895034288-my-2nd-year-chapter-4-6-hours-later")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()


driver.get("https://www.wattpad.com/896648779-my-2nd-year-chapter-5-after-1-week")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()


driver.get("https://www.wattpad.com/897330154-my-2nd-year-specials-chapter-6")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()


driver.get("https://www.wattpad.com/898580167-my-2nd-year-chapter-7")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()


driver.get("https://www.wattpad.com/899494005-my-2nd-year-chapter-8")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()


driver.get("https://www.wattpad.com/901463787-my-2nd-year-chapter-9")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()

driver.get("https://www.wattpad.com/902498234-my-2nd-year-after-an-hour-chapter-10")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()

driver.get("https://www.wattpad.com/918598116-my-2nd-year-chapter-11")
vote1=driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div[2]/button/span[2]")
vote1.click()

print("Done added 11 votes")
time.sleep(5)
driver.quit()
second_tab.quit()