import mysql.connector
import time
import os

# db = mysql.connector.connect(host="localhost", user="root", password="skilover1!", database="testdatabase")
db = mysql.connector.connect(
    host=os.getenv('MYSQLHOST'),
    user=os.getenv('MYSQLUSER'),
    port=os.getenv('MYSQLPORT'),
    password=os.getenv('MYSQLPASSWORD'),
    database=os.getenv('MYSQLDATABASE'))


cursor = db.cursor()

cursor.execute('SELECT * FROM GridTest WHERE id=1')
record = cursor.fetchone()
print(record)

db.commit()
db.close()
