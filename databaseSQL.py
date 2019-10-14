import sqlite3
import os
from sqlite3 import Error
import getch
 
 
def create_connection(DB_file):

    conn = None
    try:
        conn = sqlite3.connect(DB_file)
    except Error as e:
        print(e)
 
    return conn
 
def clearScr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def select_all(conn):
    """
    Query all rows in the tasks table
    :param conn: the Connection object
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
    
    print("\n\nPress Any key to continue")
    getch.getch()
 
 
def select_user(conn):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    clearScr()
    acc_id = int(input("Enter account number : "))
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE acc_id=?", (acc_id,))
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
 
def new_user(conn):

    cur = conn.cursor()
    clearScr()
    acc_id = int(input("Enter Account Number : "))
    acc_name = input("Enter User Name : ")
    acc_type = input("Enter Account Type (savings [s] / current [c]) : ")
    acc_balance = float(input("Enter Initial Deposit: "))

    user_data=(acc_id,acc_name,acc_type,acc_balance)

    sql_command="INSERT INTO users (`acc_id`, `acc_name`, `acc_type`, `acc_balance`) VALUES (?,?,?,?);"

    cur.execute(sql_command,user_data)
    conn.commit()
    print("User Created Successfully ")

def main():
    database = "SQL_db.db"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. New account    ")
        print("2. Account info   ")
        print("3. All accounts   ")
        print("4. New Deposit    ")
        print("5. New Withdrawal ")
        print("6. exit           ")
        Input = getch.getch()
        if Input == '1':
            new_user(conn)
        elif Input == '2':
            select_user(conn)
        elif Input == '3':
            select_all(conn)
        elif Input == '4':
            print("to be continued")
        elif Input == '5':
            print("to be continued")
        elif Input == '6':
            exit()
        else:
            print("Invalid Input")
            
        clearScr()
        main()

 
 
if __name__ == '__main__':
    main()