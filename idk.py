import mysql.connector
import getch

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
    accNo=input("Enter Acc No")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users where acc_no=%s",accNo)
    myresult = mycursor.fetchall()
    for x in myresult:
        print(x)

def Menu():
    print("Print all users if a")
    print("Print all users if b")
    choice=getch.getch()
    if choice=='a':
        printAllUsers()
    elif choice=='b':
        printUserData()
