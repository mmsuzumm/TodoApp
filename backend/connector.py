import psycopg2
from credentials import * 
from sql_queries import select
def open_connection():
    conn = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        dbname=DATABASE,
        port=PORT)
    cur = conn.cursor()
    return conn, cur




def todos_records():
    conn, cur = open_connection()
    cur.execute(select.query())
    records = cur.fetchall()
    print(records)

    cur.close()
    conn.close()
    return records

