'''Query to delete all todos'''

def query(user_id: str='NULL') -> str:
    if user_id.lower() == 'null':
        user_id = 'is null'
    else:
        # user must have only 1 id, so not "in" 
        user_id = f'= {user_id}'

    return(
    f'''
    DELETE FROM todos where 
    user_id {user_id} and
    id IS NOT NULL
    '''
    )

