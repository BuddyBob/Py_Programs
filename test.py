from flask import Flask, render_template, url_for, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import schedule 
import playsound
li = []


def search(i):
    bar = driver.find_element_by_xpath('//*[@id="yfin-usr-qry"]').send_keys(i)
    time.sleep(1)
    search_btn = driver.find_element_by_xpath('//*[@id="header-desktop-search-button"]').click()

driver =  webdriver.Chrome(executable_path='/Users/test/Desktop/chromedriver')
driver.get('https://finance.yahoo.com')
stock = 'apple'
final = search(stock)
#check for price and return
def price():

    p = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div/div/span[1]').text
    print(p)
    li.append(p)
    #check if went down or up
    plus_minus = driver.find_element_by_xpath('//*[@id="quote-header-info"]/div[3]/div/div/span[2]').text
    plus_minus = plus_minus[ 0 ]
    print(plus_minus)
    if plus_minus == '-':
        playsound.playsound('/Users/test/Documents/python/Py_Programs/music/err.mp3',False)
    if plus_minus == '+':
        playsound.playsound('/Users/test/Documents/python/Py_Programs/music/correct.mp3',False)
def listt():
    print(li)
#schedule to run
schedule.every(1).seconds.do(price)
while True:
    schedule.run_pending()
    time.sleep(2)


