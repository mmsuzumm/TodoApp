import psycopg2
import os
from psycopg2.extras import RealDictCursor  # return valid json object
from utils.format_converter import format_converter
from sql_queries.todo_queries import delete, delete_all, update_status, select_all, new_todo
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

postgres_section = config['postgres']

HOST = postgres_section['host']
# замените "os.environ.get('POSTGRES_USERNAME')" На имя пользователя вашей бд, если не хотите создавать переменные окружения
USER = os.environ.get('POSTGRES_USERNAME')
# замените "os.environ.get('POSTGRES_PASSWORD')" На Пароль пользователя вашей бд, если не хотите создавать переменные окружения
PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DBNAME = postgres_section['dbname']
PORT = postgres_section['port']


class DBConnection:
    def __enter__(self):
        self.conn = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            dbname=DBNAME,
            port=PORT)
        self.cur = self.conn.cursor(cursor_factory=RealDictCursor)
        return self.cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Error: {exc_val}")
        self.conn.commit()
        self.cur.close()
        self.conn.close()


def db_operation_todos(operation_type: str,
                       id: int | list = None,
                       user_id: int = None,
                       is_completed: bool = None,
                       todo_text: str = None
                       ):
    '''set operation_type like 
    'select_all' - select all todos from db
    'new_todo' - create new todo
    'update_status' - set status for todo by id
    'delete' - delete one or list of todos
    'delete_all' - delete all todos
    '''

    with DBConnection() as cur:
        if operation_type == 'select_all':
            cur.execute(select_all)
        elif operation_type == 'new_todo':
            cur.execute(new_todo, (is_completed, todo_text,))
        elif operation_type == 'update_status':
            if id is not None:
                cur.execute(update_status, (id,))
        elif operation_type == 'delete':
            if id is not None:
                cur.execute(delete, (id,))
        elif operation_type == 'delete_all':
            cur.execute(delete_all)

        response = cur.fetchall()
        return format_converter(response)