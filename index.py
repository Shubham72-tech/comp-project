import time
import getch
import os
import mysql.connector

cnx = mysql.connector.connect(user='compProject', password='12345678', host='eventdips.ml', database='compProject')
cursor = cnx.cursor()
selectAll="SELECT * FROM `users` WHERE 1;"

def mainMenu():
    print("a for all users")
    print("b for new user")
    option=getch.getche()
    print("\n")
    return option

def clearScreen():
    if os.name == 'nt':
        os.system('cls')  # on windows
    else:
        os.system('clear')  # on linux / os x

def sqlCon():
    cursor.execute(selectAll)
    cnx.commit()
    cursor.close()
    cnx.close()
#main
sqlCon()

