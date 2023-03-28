'''Query to update is_completed for todo'''

def query(id: int,
          is_complited: bool,
          user_id: str='NULL') -> str:
    
    if is_complited:
        is_complited = False
    else:
        is_complited = True
        
    if user_id.lower() == 'null':
        user_id = 'is null'
    else:
        # user must have only 1 id, so not "in" 
        user_id = f'= {user_id}'

    return(
    f'''
    UPDATE todos 
    SET is_complited = {is_complited} where id = {id}
    RETURNING id, is_complited
    '''
    )

