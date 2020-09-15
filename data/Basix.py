#Import build in module
import sqlite3
from sqlite3 import Error
#Create class of employees
class Emp:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
#Create an object for the class xxxaining the attributes first name, last name and pay
emp1 = Emp("Thavas","Antonio",90000)
emp2 = Emp("Thaze","Antonio",90000000)
#Connect to db, memory is used for testing
#It will erase the database everytime you run it
#So you have a new one everytime
#If you dont want it to be errased you can just replace it with a file name.db
conn = sqlite3.connect('basix.db')
#This variable will let you insert data into the db
c = conn.cursor()
#This try and except is not nessaccary but if you do not
#Set line 16 to 'memory it will return an error
#* The table has already been created *#
try:
    c.execute("""CREATE TABLE employees(
        first text,
        last text,
        pay integer
        )""")
except:
    print('table already exists')
#How to insert values into the table
#:first ,:last, :pay are place holders
# You enter the values for them as a dictionary on the right seperated by a comma
#emp1.first, emp1.last, emp1.pay are objects for a class created above
c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':emp1.first,'last':emp1.last,'pay':emp1.pay})
#Always commit your changes
conn.commit()
c.execute("INSERT INTO employees VALUES (:first,:last,:pay)",{'first':emp2.first,'last':emp2.last,'pay':emp2.pay})
conn.commit()
#One way of reading all the rows in the file
def get_posts():
    with conn:
        c.execute("SELECT * FROM employees")
        print(c.fetchall())
#run the function
get_posts()
#Check for 'ANTONIO' in the 'last' columm
c.execute("SELECT * FROM employees WHERE last='Antonio'")
#fetch all will get everything that meets your requirements
#fetch many requires and input of how many you would like to see
#fetch on will only recieve one of the rows
print(c.fetchall())
#CLOSE
conn.close()
