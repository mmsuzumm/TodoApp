'''Query to select todos'''

def query(user_id: str='NULL'):
    if type(user_id) == str or type(user_id) == int:
        user_id = str(user_id)

        # is psql when null you need to use "IS NULL"
        # and with correct id u must use equals
        # temporary solution. Later, the user will always have an id
        if user_id.lower() == 'null':
            user_id = 'is null'
        else:
            # user must have only 1 id, so not "in" 
            user_id = f'= {user_id}'

        return(
        f'''
            SELECT id, user_id, is_complited, todo_text 
            FROM todos
            WHERE user_id {user_id};
        '''
        )
    else:
        return 'Error: wrong data type'
