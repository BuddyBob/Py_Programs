from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import smtplib
import os

import playsound
playsound.playsound('song.mp3',False)
print ('...')

f = open("DailyStuff.txt","w")
f.write("Good Morning! How Are You \n")


driver =  webdriver.Chrome(executable_path='/Users/test/Desktop/chromedriver')
value1 = '$69.99'
value2 = '$79.99'


#DRONES
#get link
driver.get('https://www.amazon.com/SIMREX-Positioning-Quadcopter-Altitude-Headless/dp/B07SX1Z9WK/ref=sr_1_1_sspa?dchild=1&keywords=Drone&qid=1590787022&sr=8-1-spons&psc=1&smid=A2SENA2R5CYMSA&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFXM1JINFM0Q1lGTFImZW5jcnlwdGVkSWQ9QTAwNTQyMzNQNE1YVVI1MDFORVEmZW5jcnlwdGVkQWRJZD1BMDA5ODE1MFA3WTlBMzlNSFZTTSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU=')
driver.maximize_window()
#drone1
print("[Product: SIMREX X900 Drone]")
#check_price/print_price
price = driver.find_elements_by_id('priceblock_saleprice')
for value in price:
    print("The Original Price Was: "+str(value1))
    print("The Price Today Is: "+str(value.text))
    box = value.text
   
print("--------------------------------------------------------------------------------------------------------------")



#Drone 2
print("[Product: SNAPTAIN S5C WiFi FPV Drone]")
driver.get('https://www.amazon.com/SNAPTAIN-Wide-Angle-Quadcopter-Altitude-Compatible/dp/B07GPNZSMY/ref=sr_1_2?dchild=1&keywords=Drone&qid=1590805637&sr=8-2')

#check_price/print_price
price2 = driver.find_elements_by_id('priceblock_ourprice')
#print prices
for value in price2:
    print("The Original Price Was: "+str(value2))
    print("The Price Today Is: "+str(value.text))


print("------------------------------------------------------------------------------------------------------")


#Date
driver.get('https://www.google.com/?gws_rd=ssl')
q = driver.find_element_by_name('q')
q.send_keys('Date')
q.send_keys(Keys.ENTER)

date = driver.find_element_by_xpath('//*[@id="rso"]/div[1]/div/div[1]/div')
print("The date today is: "+str(date.text))
#write to text file/date
print('--------------------------------------------------------------------------------------------------------')


#Temp
time.sleep(2)
driver.get('https://www.bing.com/search?q=weather%20today&pc=cosp&ptag=G6C15N11104D041620AA6B84BBD86&form=CONBDF&conlogo=CT3210127')
temp = driver.find_element_by_xpath('//*[@id="b_results"]/li[1]/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]')
look = driver.find_element_by_xpath('//*[@id="b_results"]/li[1]/div/div/div[1]/div[2]/div[2]/div[2]/div[1]')
print("The temperature is: "+str(temp.text)+" and it looks: "+str(look.text))
print("---------------------------------------------------------------------------------------------------------")
driver.quit()
