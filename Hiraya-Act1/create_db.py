import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "LRMA02132389*",
    )

my_cursor = mydb.cursor()

my_cursor.execute("CREATE DATABASE Sched2")

if my_cursor:
    print("Database created successfully")
else:
    print("Error creating database")