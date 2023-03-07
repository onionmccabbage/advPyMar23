import sqlite3

def main():
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # ask user for valid value of userId
    invalid = True
    while invalid:
        u = int(float(input('User Id?')))
        if type(u) == int and u > 0:
            invalid = False
    # use '?' as a placeholder in SQL statements
    st = '''
    SELECT userID, id, title, body FROM posts
    WHERE userID=?
    '''
    # execute
    try:
        rows = curs.execute(st, (u,)) # arguments must be a tuple
        for item in rows:
            print('Item {} (user {}) title:{}'
                .format(item[1], item[0], item[2]))
    except Exception as err:
        print('There was a problem:{}'.format(err))
    conn.close() # always make sure the connection is closed
    
if __name__ == '__main__':
    main()