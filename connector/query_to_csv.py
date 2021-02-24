import mysql.connector
import csv
import os
from pathlib import Path


def upgrade_tasks():
    my_db = mysql.connector.connect(
        host=os.environ['MYSQL_HOST'],
        port=int(os.environ['MYSQL_PORT']),
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASS'],
        database=os.environ['MYSQL_DB']
    )

    my_cursor = my_db.cursor()
    my_cursor.execute(
        "SELECT id, name, TIMESTAMPDIFF(MINUTE, start_at, end_at) times, owner_id FROM section_card_task WHERE status = 6 AND start_at < end_at;")

    field_names = [i[0] for i in my_cursor.description]
    rows = my_cursor.fetchall()
    rows.insert(0, field_names)

    if os.path.exists("/app/data/tasks.csv"):  # removing file
        os.remove("/app/data/tasks.csv")

    Path("/app/data").mkdir(parents=True, exist_ok=True)

    fp = open('/app/data/tasks.csv', 'w')
    myFile = csv.writer(fp)
    myFile.writerows(rows)
    fp.close()


upgrade_tasks()
