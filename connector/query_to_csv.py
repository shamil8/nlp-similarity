import mysql.connector
import sys
import csv
import os
from pathlib import Path
from nlp_py.constants import TASK_VERIFIED
import constants.duration as du


def upgrade_tasks():
    my_db = mysql.connector.connect(
        host=os.environ['MYSQL_HOST'],
        port=int(os.environ['MYSQL_PORT']),
        user=os.environ['MYSQL_USER'],
        password=os.environ['MYSQL_PASS'],
        database=os.environ['MYSQL_DB']
    )

    query_str = "SELECT id, name, IF(duration = '0м', TIMESTAMPDIFF(MINUTE, start_at, end_at), duration) AS times, owner_id \
        FROM section_card_task  \
        WHERE status = %(status)s  \
        AND start_at < end_at"

    params = {
        'status': TASK_VERIFIED
    }

    my_cursor = my_db.cursor()
    my_cursor.execute(query_str, params)

    field_names = [i[0] for i in my_cursor.description]
    rows = my_cursor.fetchall()

    # Convert the tuple (rows) into a list to be able to change it:
    for idx, row in enumerate(rows):
        if type(row[2]) is str:  # third element it's duration (or times)
            rowList = list(row)
            duration_arr = rowList[2].split()

            minutes = 0
            for duration in duration_arr:
                if duration.find(du.SIGN_WEEK) != -1:
                    weeks = int(duration[:duration.find(du.SIGN_WEEK)])
                    minutes += weeks * du.WEEK_WORK_DAYS * du.DAY_WORK_HOURS * du.HOUR_TO_MINUTES

                elif duration.find(du.SIGN_DAY) != -1:
                    days = int(duration[:duration.find(du.SIGN_DAY)])
                    minutes += days * du.DAY_WORK_HOURS * du.HOUR_TO_MINUTES

                elif duration.find(du.SIGN_HOUR) != -1:
                    hours = int(duration[:duration.find(du.SIGN_HOUR)])
                    minutes += hours * du.HOUR_TO_MINUTES

                elif duration.find(du.SIGN_MINUTE) != -1:
                    minutes += int(duration[:duration.find(du.SIGN_MINUTE)])

                else:
                    try:
                        minutes += int(duration)
                    except ValueError as e:
                        print('I got a ValueError - reason "%s"' % str(e), file=sys.stderr)

            rowList[2] = minutes
            rows[idx] = tuple(rowList)

            print(duration_arr, minutes, ' duration to minutes', file=sys.stderr)

    rows.insert(0, field_names)

    if os.path.exists("/app/data/tasks.csv"):  # removing file
        os.remove("/app/data/tasks.csv")

    Path("/app/data").mkdir(parents=True, exist_ok=True)

    fp = open('/app/data/tasks.csv', 'w')
    myFile = csv.writer(fp)
    myFile.writerows(rows)
    fp.close()


upgrade_tasks()
