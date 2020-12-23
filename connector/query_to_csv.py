import mysql.connector
import csv

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='initiator'
)

my_cursor = my_db.cursor()
my_cursor.execute("SELECT * FROM section_card_task WHERE status = 6;")

rows = my_cursor.fetchall()

fp = open('/app/data/file.csv', 'w')
myFile = csv.writer(fp)
myFile.writerows(rows)
fp.close()
