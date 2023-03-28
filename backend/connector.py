import psycopg2
from psycopg2.extras import RealDictCursor # return valid json object
from credentials import * 
from sql_queries import select, insert, delete
from utils.format_converter import format_converter


def open_connection():
    conn = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        dbname=DATABASE,
        port=PORT)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur


# def execute_query(query_type):
#     conn, cur = open_connection()
#     cur.execute(query_type.query())
#     conn.commit()
#     response = cur.fetchall()
#     cur.close()
#     conn.close()
#     return format_converter(response)

def todos_records() -> str:
    conn, cur = open_connection()
    cur.execute(select.query())
    records = cur.fetchall()
    cur.close()
    conn.close()
    return format_converter(records)

def todo_writer(is_completed: str, todo_text: str) -> str:
    conn, cur = open_connection()
    cur.execute(insert.query(is_completed, todo_text))
    conn.commit()
    new_record = cur.fetchall()
    cur.close()
    conn.close()
    return format_converter(new_record)

def todo_deleter(index) -> str:
    conn, cur = open_connection()
    cur.execute(delete.query(index))
    conn.commit()
    response = cur.fetchall()
    cur.close()
    conn.close()
    return format_converter(response)