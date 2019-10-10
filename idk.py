import mysql.connector
import os
import getch
import time

mydb = mysql.connector.connect(
  host="localhost",
  user="compProject",
  passwd="12345678",
  database="compProject"
)
def printAllUsers():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def printUserData():
    accNo=input("Enter Acc No ---> ")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE acc_no = %s"
    query = (accNo,)
    mycursor.execute(sql,query)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def Menu():
    print("all users if a")
    print("users by acc No if b")
    print("Press q to exit")
    print("--->")
    choice=getch.getch()
    if choice=='a':
        printAllUsers()
    elif choice=='b':
        printUserData()
    elif choice=='q':
        exit()
    else:
         print("Try Again or press q to quit ")
         time.sleep(5)
         if os.name == 'nt':
             os.system('cls')
         else:
             os.system('clear')
	 Menu()
#main
Menu()
