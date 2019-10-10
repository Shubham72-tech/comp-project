import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="compProject",
  passwd="12345678",
  database="compProject"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM users")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
