import sqlite3
import random
conn = sqlite3.connect('startest.db')
c = conn.cursor()
try:
    c.execute("""CREATE TABLE starInfo(
                username text,
                password text
            )""") 
except sqlite3.OperationalError: pass
def login():
    username = input('Login: ')
    pwd = input('Password: ')
    findUser = ("SELECT * FROM starInfo WHERE username=?,password=?",(username,pwd))
    conn.commit()
    result = c.fetchall()
    print(result)
    if result == []:
        c.execute("INSERT INTO starInfo VALUES (?,?)",(username,pwd))
        conn.commit()
        c.execute("SELECT * FROM starInfo WHERE username=?, password=?",(username,pwd))
        print(c.fetchall())
login()
conn.close()