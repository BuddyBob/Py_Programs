#import modules
import sqlite3
import random
import time
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
login = (input('Enter your login information: '))
#Look for there user name
findUser = ("SELECT * FROM yui_stats WHERE username=?")
conn.commit()
c.execute(findUser,[login])
result = c.fetchall()
print(result)
#choose random ores based on percent
oreList = ['copper'] * 80 + ['silver'] * 18 + ['gold'] * 2


#empty database?
c.execute("select count(*) from yui_stats")
empty = c.fetchall()
if empty == [(0,)]:
    copper = 0
    silver = 0
    gold = 0
else:
    #retrive data
    with conn:
        c.execute("SELECT * FROM yui_stats")
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
def hasNumbers(inputString):
    return all(char.isdigit() for char in inputString)
#you have not played   
if len(result) == 0:
    c.execute("INSERT INTO yui_gamesplayed VALUES (:player,:games)",{'player':login,'games':1})
else:
    c.execute("UPDATE yui_gamesplayed SET player=?,games=? WHERE player=?",(login,2,login))
conn.commit()
c.execute("SELECT * FROM yui_gamesplayed WHERE player='{}'".format(login))
conn.commit()
li = c.fetchall()
tup = li[0]
games = tup[1]
while True:
    #user choice of what too do
    print(''' 
    

    ''')
    yui = (input(': '))
    #if user chooses to mine
    if yui == 'y':
        #choose an ore
        ores = random.choice(oreList)
        print(ores)
        #print what they got
        if ores == 'copper':
            print('You struck copper and received {} copper coins'.format(1000))
            copper+=1000
        if ores == 'silver':
            print('You struck silver and received {} silvers'.format(100))
            silver+=100
        if ores == 'gold':
            print('You struck gold and received {} gold nuggets'.format(20))
            gold+=20
    #slowmow
    def slowmow(yui):
        if yui == '!slow-mow':
            yui = (input('        : '))
            if hasNumbers(yui) == True:
                global timer
                timer = yui
                if timer > 1:
                    print('timer changed')
                else:
                    timer = 2
                    print('timer was bumped up (it was too low)')
    slowmow(yui)


    if yui == 'quit':
        #Insert there balance
        #check if database is empty
        c.execute("select count(*) from yui_stats")
        empty = c.fetchall()[0]
        #if it is, insert values
        if games == 1:
            c.execute("INSERT INTO yui_stats VALUES (:username,:copper,:silver,:gold)",{'username':login,'copper':copper,'silver':silver,'gold':gold})
        #if it is not, update data
        if games == 2:
            c.execute("UPDATE yui_stats SET username=?,copper=?, silver=?, gold=? WHERE username=?",(login,copper,silver,gold,login))
        conn.commit()

        with conn:
            c.execute("SELECT * FROM yui_stats WHERE username='{}'".format(login))
            print(c.fetchall())
        c.execute("SELECT * FROM yui_stats")
        print(c.fetchall())
        exit()
    try:
        time.sleep(timer)
    except NameError:
        timer = 4
        time.sleep(timer)
conn.close()
c.close()


