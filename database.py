import mysql.connector
from datetime import datetime

from datetime import date

cnx = mysql.connector.connect(
    user='root',
    password='aksh1310',
    host='127.0.0.1',
    database='face_attendance'
)
def mark_attendance(name):
    cursor = cnx.cursor()
    now = datetime.now()
    today_date = now.date()
    today_time = now.strftime("%H:%M:%S")
    cursor.execute("INSERT INTO detection (name, date, time) VALUES (%s, %s, %s)", (name, today_date, today_time))
    cnx.commit()
    cursor.close()


def get_attendance():
    cursor = cnx.cursor()
    today = date.today()
    cursor.execute("SELECT * FROM detection WHERE date=%s",(today,))
    results=cursor.fetchall()
    cursor.close()
    return results
   
