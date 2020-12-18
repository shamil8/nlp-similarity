import mysql.connector
import csv

mydb = mysql.connector.connect(
    host='mysql',
    user='root',
    password='root',
    database='initiator'
)

mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM tasks;')

rows = mycursor.fetchall()

fp = open('/app/data/file.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
