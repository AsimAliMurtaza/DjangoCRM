import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'OqixpAC@!gP_M8M'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE myDatabase")

print("ALL DONE!")