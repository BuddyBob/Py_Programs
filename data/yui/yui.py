import sqlite3
import random
import time
import picaxes
from colorama import Fore
import datetime
from datetime import datetime,timedelta,date
from workers import lazyworker,hardworker,worker

BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
#connect
conn = sqlite3.connect('yui.db')
#create cursor
c = conn.cursor()

#create table with copper silver and gold


try:
    c.execute("""CREATE TABLE yui_stats(
                username text,
                copper integer,
                silver integer,
                gold integer
            )""") 

except sqlite3.OperationalError: pass
#Ask for login
login = (input('Enter your login information 🔐: '))
#Look for there user name
findUser = ("SELECT * FROM yui_stats WHERE username=?")
conn.commit()
c.execute(findUser,[login])
result = c.fetchall()

#choose random ores based on percent
oreList = ['copper'] * 80 + ['silver'] * 28 + ['gold'] * 2


#empty database?
c.execute("select * from yui_stats where username='{}'".format(login))
empty = c.fetchall()

if empty == []:
    copper = 0
    silver = 0
    gold = 0
else:
    #retrive data
    with conn:
        c.execute("SELECT * FROM yui_stats WHERE username='{}'".format(login))
        tup = c.fetchall()

        for t in tup:
            copper = t[1]
            silver = t[2]
            gold = t[3]     

#Count players games
try:
    c.execute("""CREATE TABLE yui_gamesplayed(
                player text,
                games integer
            )""") 

except sqlite3.OperationalError: pass

try:
    c.execute("""CREATE TABLE yui_pics(
                player text,
                cpic text,
                spic text,
                gpic text
            )""") 

except sqlite3.OperationalError: pass
try:
    c.execute("""CREATE TABLE yui_workers(
        player text,
        lazyworker integer,
        worker integer,
        hardworker integer,
        date text
    )""")
except sqlite3.OperationalError: pass
conn.commit()
def hasNumbers(inputString):
    return all(char.isdigit() for char in inputString)
#you have not played   
if len(result) == 0:
    c.execute("INSERT INTO yui_gamesplayed VALUES (:player,:games)",{'player':login,'games':1})
    conn.commit()
    #Insert beginner pic levels
    c.execute("INSERT INTO yui_pics VALUES (?,?,?,?)",(login,'level1','level1','level1'))
    conn.commit()
    presentday = date.today()
    c.execute("INSERT INTO yui_workers VALUES (?,?,?,?,?)",(login,10,10,10,presentday))
    conn.commit()
else:
    c.execute("UPDATE yui_gamesplayed SET player=?,games=? WHERE player=?",(login,2,login))
    conn.commit()
c.execute("SELECT * FROM yui_gamesplayed WHERE player='{}'".format(login))
conn.commit()
li = c.fetchall()
tup = li[0]
games = tup[1]
#Get pic levels and store in variables
c.execute("SELECT * FROM yui_pics WHERE player='{}'".format(login))
conn.commit()
tup2 = c.fetchone()
print(tup2)
copperPic = tup2[1]
silverPic = tup2[2]
goldPic = tup2[3]
#WORKERS
c.execute("SELECT * FROM yui_workers WHERE player='{}'".format(login))
conn.commit()
tup3 = c.fetchone()
print('dates: '+str(tup3))
#get worker count
lzyworker = tup3[1]
wrker = tup3[2]
hardwrker = tup3[3]
#get today date
datetoday = tup3[4]
datetoday = datetime.strptime(datetoday, '%Y-%m-%d')
datetoday = datetoday.date()
while True:
    #user choice of what too do
    print(''' 
    
    ''')
    yui = (input(': '))
    #if user chooses to mine
    if yui == 'y':
        #choose an ore
        levelAmountCopper = {'level1':10000,'level2':100000,'level3':400000,'level4':1000000,'level5':4000000}
        levelAmountSilver = {'level1':100,'level2':2000,'level3':4000,'level4':10000,'level5':100000}
        levelAmountGold = {'level1':20,'level2':500,'level3':1000,'level4':5000,'level5':10000}
        ores = random.choice(oreList)
        #print what they got
        if ores == 'copper':
            print('You struck '+str(BOLD+UNDERLINE)+'copper'+str(END)+' and received {} copper coins'.format(BOLD+UNDERLINE+str(levelAmountCopper.get(copperPic))+END))
            copper += int(levelAmountCopper.get(copperPic))
        if ores == 'silver':
            print('You struck '+str(BOLD+UNDERLINE)+'silver'+str(END)+' and received {} silvers'.format(BOLD+UNDERLINE+str(levelAmountSilver.get(silverPic))+END))
            silver+=int(levelAmountSilver.get(silverPic))
        if ores == 'gold':
            print('You struck '+str(BOLD+UNDERLINE)+'gold'+str(END)+' and received {} gold nuggets'.format(BOLD+UNDERLINE+str(levelAmountGold.get(copperPic))+END))
            gold+=int(levelAmountGold.get(copperPic))
    def daily():
        
        global datetoday
        global silver
        dateNow = date.today()
        if dateNow == datetoday:
            datetoday=datetime.today() + timedelta(days=1)
            datetoday = datetoday.date()
            c.execute("UPDATE yui_workers SET date=? WHERE player=?",(datetoday,login))
            conn.commit()
            chosenworkers = random.choice(['lazyworker'])
            print(lzyworker)
            if chosenworkers == 'lazyworker':
                addamount = lazyworker(lzyworker)
            if chosenworkers == 'worker':
                addamount = worker(wrker)
            if chosenworkers == 'hardworker':
                addamount = hardworker(hardwrker)
            silver += int(addamount)
        elif dateNow > datetoday:
            datetoday = datetime.today() + timedelta(days=1)
            datetoday = datetoday.date()
            c.execute("UPDATE yui_workers SET date=? WHERE player=?",(datetoday,login))
            conn.commit()
            silver += addamount
        else:
            print('WAIT... JESUS MAN')

    def slowmow(yui):
        if yui == '!slow-mow':
            yui = (input('        : '))
            if hasNumbers(yui) == True:
                global timer
                timer = int(yui)
                if timer > 1:
                    print('⏰ | timer '+str(BOLD)+'changed'+str(END))
                else:
                    timer = 2
                    print('⏰ | timer was '+str(BOLD)+' bumped up '+str(END)+'(it was too low)')
            if yui == 'time':
                try:
                    print('The time is set to '+str(timer))
                except NameError:
                    print('The time is set to '+str(BOLD)+'1'+str(END))
    slowmow(yui)
    def flip():
        global silver
        #options
        opt = ['heads','tails']
        #choose from list
        side = random.choice(opt)
        yuiSide = (input('        : '))
        if yuiSide in opt:
                
            yuiBet = int(input('                : '))
            if yuiBet < 100 or yuiBet > silver:
                print('🚫 | '+str(BOLD)+'Invalid'+str(END)+' Bet')
            else:
                if yuiSide == side:
                    print('🎉💰| »»'+str(BOLD)+'CORRECT'+str(END)+'«« | You Guessed {} and Flipped {}'.format(BOLD+UNDERLINE+yuiSide+END+END,BOLD+UNDERLINE+side+END+END))
                    silver += yuiBet
                if yuiSide != side:
                    print('🚫 | »»'+str(BOLD)+'INCORRECT'+str(END)+'«« | You Guessed {} and Flipped {}'.format(BOLD+UNDERLINE+yuiSide+END+END,BOLD+UNDERLINE+side+END+END))
                    silver -= yuiBet
        else:
            print('🚫 | Plz enter »»heads«« or »»tails««')
    def exchange():
        #1000 copper == 10 silver
        #20 gold == 1000 silver
        global silver
        global copper
        global gold
        silver += copper * 10 / 1000
        copper = 0
    def picPrices():
        return \
        '''
        ---------------------------------------------- ----------------------------------------------
        === 💳 Copper Pics: '''+str(copperCostOfPic)+'''|
        ---------------------------------------------- ----------------------------------------------
        === 💳 Silver Pics: '''+str(silverCostOfPic)+'''|
        ---------------------------------------------- ----------------------------------------------
        === 💳 Gold Pics: '''+str(goldCostOfPic)

    def buyPics(yui):
        global silver
        global gold
        global copperPic
        global silverPic
        global goldPic
        global copperCostOfPic
        global silverCostOfPic
        global goldCostOfPic
        copperCostOfPic = {'level2':10000,'level3':100000,'level4':1000000,'level5':1000000000}
        silverCostOfPic = {'level2':50000,'level3':200000,'level4':5000000,'level5':9999999999}
        goldCostOfPic = {'level2':400,'level3':1000,'level4':5000,'level5':1000000}
        global copperPic
        if yui == 'yui buy pic':
            yuiPic = (input('       :'))
            if yuiPic == 'copper':
                cpic = picaxes.pic(copperPic)
                checkPic = cpic.copper_pic()
                if silver >= copperCostOfPic.get(checkPic):
                    silver -= copperCostOfPic.get(checkPic)
                    cpic = picaxes.pic(copperPic)
                    copperPic = cpic.copper_pic()
                    print(copperPic)
                else:
                    print('🚫| Insufficiant Ballance '+str(BOLD+UNDERLINE)+'('+str(copperCostOfPic.get(checkPic))+')'+str(END))
            if yuiPic == 'silver':
                spic = picaxes.pic(silverPic)
                checkPic = spic.silver_pic()
                if silver >= silverCostOfPic.get(checkPic):
                    silver -= silverCostOfPic.get(checkPic)
                    spic = picaxes.pic(checkPic)
                    silverPic = spic.silver_pic()
                    print(silverPic)
                else:
                    print('🚫| Insufficiant Ballance '+str(BOLD+UNDERLINE)+'('+str(silverCostOfPic.get(checkPic))+')'+str(END))
            if yuiPic == 'gold':
                #Find the next level
                gpic = picaxes.pic(goldPic)
                checkPic = gpic.gold_pic()
                #Check if you have enough gold
                if gold >= goldCostOfPic.get(checkPic):
                    #subtract gold of next level
                    gold -= goldCostOfPic.get(checkPic)
                    #create an object and find the next level of your pic
                    gpic = picaxes.pic(goldPic)
                    #call the function in pic class
                    goldPic = gpic.gold_pic()
                    print(goldPic)
                else:
                    print('🚫| Insufficiant Ballance '+str(BOLD+UNDERLINE)+'('+str(goldCostOfPic.get(checkPic))+')'+str(END))
            
        
    buyPics(yui)
    def bal():
        print('––––––––––––––––––––––💰–––––––––––––––––––––––––––')
        print('copper '+str(BOLD)+'['+str(copper)+']'+str(END))
        print('       silver '+str(BOLD)+'['+str(silver)+']'+str(END))
        print('              gold '+str(BOLD)+'['+str(gold)+']'+str(END))
        print('––––––––––––––––––––––💰––––––––––––––––––––––––––')
    def deleteUser():
        yuiDel = (input('          :'))
        if yuiDel == login:
            print('''You cannot '''+str(BOLD)+'''delete'''+str(END)+''' yourself LOL
            thats suicide
            you may create another account and kill {}'''.format(yuiDel))
        else:
            c.execute("DELETE FROM yui_stats WHERE username='{}'".format(yuiDel))
            conn.commit()
        
    if yui == '!del user' or yui == '!delete user':
        deleteUser()
        print('🚫 | '+str(BOLD)+'Deleted User'+str(END))

    if yui == 'yui exchange':
        exchange()
        print('✅ | '+str(BOLD)+'Exchanged'+str(END))
        bal()

    if yui == 'yui bal' or yui == 'yui balance':
        bal()

    if yui == 'yui flip':
        flip()  
    if yui == 'yui pic prices':
        print(picPrices())
    if yui == 'yui daily':
        daily()
    if yui == 'quit':
        #Insert there balance
        #check if database is empty
        c.execute("select count(*) from yui_stats")
        empty = c.fetchall()[0]
        #if it is, insert values
        if games == 1:
            c.execute("INSERT INTO yui_stats VALUES (:username,:copper,:silver,:gold)",{'username':login,'copper':copper,'silver':silver,'gold':gold})
            c.execute("UPDATE yui_pics SET player=?, cpic=?, spic=?, gpic=?",(login,copperPic,silverPic,goldPic))
        #if it is not, update data
        if games == 2:
            c.execute("UPDATE yui_pics SET player=?, cpic=?, spic=?, gpic=?",(login,copperPic,silverPic,goldPic))
            conn.commit()
            c.execute("SELECT * FROM yui_pics WHERE player='{}'".format(login))
            conn.commit()
            tup2 = c.fetchone()
            print(tup2)
            c.execute("UPDATE yui_stats SET username=?,copper=?, silver=?, gold=? WHERE username=?",(login,copper,silver,gold,login))
        conn.commit()

        with conn:
            c.execute("SELECT * FROM yui_stats WHERE username='{}'".format(login))
            print(c.fetchall())
        c.execute("SELECT * FROM yui_stats")
        print(c.fetchall())
        exit()
    try:
        for i in range(1,timer+1):
            print(i)
            time.sleep(1)
    except NameError:
        timer = 4
        for i in range(1,timer+1):
            print(i)
            time.sleep(1)
conn.close()
c.close()