import psycopg2
from psycopg2.extras import RealDictCursor # return valid json object
from credentials import * 
from utils.format_converter import format_converter
from sql_queries.todo_queries import delete, delete_all, update_status, select_all, new_todo

def open_connection():
    conn = psycopg2.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        dbname=DATABASE,
        port=PORT)
    cur = conn.cursor(cursor_factory=RealDictCursor)
    return conn, cur

def db_operation_todos(operation_type: str, 
                  id: int | list=None, 
                  user_id: int=None,
                  is_completed: bool=None,
                  todo_text: str=None
                 ):
    '''set operation_type like 
    'select_all' - select all todos from db
    'new_todo' - create new todo
    'update_status' - set status for todo by id
    'delete' - delete one or list of todos
    'delete_all' - delete all todos
    '''

    conn, cur = open_connection()
    if operation_type == 'select_all':
        cur.execute(select_all)
    if operation_type == 'new_todo':
        cur.execute(new_todo, (is_completed, todo_text,))
    if operation_type == 'update_status':
        cur.execute(update_status, (id,))
    if operation_type == 'delete':
        cur.execute(delete, (id,))
    if operation_type == 'delete_all':
        cur.execute(delete_all)
        
    conn.commit()
    response = cur.fetchall()
    cur.close()
    conn.close()
    return format_converter(response)