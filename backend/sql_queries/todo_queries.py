# all queries. Later add user_id

select_all = '''SELECT id, user_id, is_completed, todo_text 
    FROM todos
    ORDER BY id;'''

new_todo = '''INSERT INTO todos (is_completed, todo_text) 
    VALUES (%s, %s) 
    RETURNING id, user_id, is_completed, todo_text;
'''

update_status = '''UPDATE todos 
    SET is_completed = NOT is_completed
    WHERE id = %s
    RETURNING id, is_completed'''

delete = '''
    DELETE FROM todos where id = ANY(%s)
    RETURNING id, user_id
    '''

delete_all = '''
    DELETE FROM todos where
        id IS NOT NULL
    RETURNING 'Ok'
    '''