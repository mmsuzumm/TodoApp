'''Query to select todos'''

def query(user_id: str='NULL') -> str:
    if user_id.lower() == 'null':
        user_id = 'is null'
    else:
        # user must have only 1 id, so not "in" 
        user_id = f'= {user_id}'

    return(
    f'''
    SELECT id, user_id, is_complited, todo_text 
    FROM todos
    WHERE user_id {user_id}
    ORDER BY id;
    '''
    )

