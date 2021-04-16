from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from colorama import Fore, Back, Style
import numpy as np
import requests
import time
import os
previous = [0]
previous2 = [0]
previous3 = [0]
totalPrices = []
prices = {}
def stockies(to_watch, ticker=2, returnOnChange=True):
    global previous,previous2,previous3,prices,totalPrices
    try:
        os.remove('./stuffies.txt')
    except:
        pass
    def getPrice(to_watch,firstTime):
        global previous,previous2
        while True:
            try:
                client = urlopen(f'https://finance.yahoo.com/quote/{to_watch}')
                pageSource = client.read()
                client.close()
                mixedSoup = soup(pageSource,"html.parser")
                price = mixedSoup.findAll("span",{"class":"Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
                "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"
                pp = price[0].text.strip()
                pp = pp.replace(',','')
                break
            except IndexError:
                pass
        #check if first time looking
        if firstTime == True:
            #set previous
            previous[0] = float(pp)
            #return stock
            return float(pp)
        if returnOnChange == True:
            #check if price changed
            if float(pp) not in previous:
                #set new price
                previous[0] = float(pp)
                return float(pp)
            #price hasnt changed, reload page and check again, parameter not first time set
            else:
                return getPrice(to_watch,False)
                
        else:
            greaterThan = False
            if float(pp) > previous2[0]:
                greaterThan = True
            previous2[0] = float(pp)
            if greaterThan == True:
                return str(float(pp))
            else:
                return str(float(pp))
    try:
        count = 0
        while True:
            if count == 0:
                prices[to_watch] = getPrice(to_watch,True)
                count += 1
            else:
                prices[to_watch] = getPrice(to_watch,False)
            pp = float(list(prices.values())[0])
            totalPrices.append(pp)
            if previous3[0] > float(pp):
                print("{"+Fore.RED+str(list(prices.keys())[0])+Style.RESET_ALL+" : $ "+Style.RESET_ALL+Fore.RED+str(list(prices.values())[0])+Style.RESET_ALL+"}  (↓) diff: "+Fore.YELLOW+str(round(previous3[0]-pp,3)*-1)+Style.RESET_ALL)
            else:
                print("{"+Fore.RED+str(list(prices.keys())[0])+Style.RESET_ALL+" : $ "+Style.RESET_ALL+Fore.GREEN+str(list(prices.values())[0])+Style.RESET_ALL+"}  (↑) diff: "+Fore.YELLOW+'+'+str(round(previous3[0]-float(pp),3)*-1)+Style.RESET_ALL)
            previous3[0] = float(pp)
            time.sleep(ticker)
    except (KeyboardInterrupt):
            file = open('stuffies.txt','a+')
            stock = str(list(prices.keys())[0])
            Change = round(totalPrices[-1]-totalPrices[0],3)
            totalPrices = sorted(totalPrices)
            highest = totalPrices[-1]
            lowest = totalPrices[0]
            file.write('\n\n'+stock+'\n[\nChange: '+str(Change)+'\nHighest:'+str(highest)+'\nLowest: '+str(lowest)+'\n]')
            file.close()
