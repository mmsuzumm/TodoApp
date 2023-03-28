'''Query to insert todo'''

def query(is_completed: str,
          todo_text: str,
          user_id: str='NULL') -> str:
    if user_id.lower() == 'null':
        user_id = 'is null'
    else:
        # user must have only 1 id, so not "in" 
        user_id = f'= {user_id}'

    return(
    f'''
    INSERT INTO todos (is_completed, todo_text) 
    VALUES ({is_completed}, '{todo_text}') 
    RETURNING id, user_id, is_completed, todo_text;
    '''
    )

