'''Query to update is_completed for todo'''

def query(id: int,
          is_completed: bool,
          user_id: str='NULL') -> str:
    
    if is_completed:
        is_completed = False
    else:
        is_completed = True
        
    if user_id.lower() == 'null':
        user_id = 'is null'
    else:
        # user must have only 1 id, so not "in" 
        user_id = f'= {user_id}'

    return(
    f'''
    UPDATE todos 
    SET is_completed = {is_completed} where id = {id}
    RETURNING id, is_completed
    '''
    )

