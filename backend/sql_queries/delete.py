'''Query to delete todo or todos'''

def query(id: int | list, 
          user_id: str='NULL') -> str:
    if user_id.lower() == 'null':
        user_id = 'is null'
    else:
        # user must have only 1 id, so not "in" 
        user_id = f'= {user_id}'
    if type(id) == list:
        id = ', '.join(map(str, id))

    return(
    f'''
    DELETE FROM todos where id in ({id})
    RETURNING id, user_id
    '''
    )

