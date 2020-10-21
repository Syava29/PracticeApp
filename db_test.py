import sqlite3

conn = sqlite3.connect("data/db_data.db")
cursor = conn.cursor()

def sql_fetch(conn):

    cursorObj = conn.cursor()

    cursorObj.execute('SELECT discip FROM discip WHERE id_prepod == 1')

    rows = cursorObj.fetchall()

    for row in rows:

        print(row)

sql_fetch(conn)