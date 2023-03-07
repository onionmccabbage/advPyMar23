import sqlite3

def main():
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # ask user for valid value of userID
    invalid = True
    while invalid:
        u = int(float(input('User ID?')))
        if type(u) == int and u > 0:
            invalid = False
    # use '?' as a placeholder in SQL statements
    st = '''
    SELECT userID, id, title, completed FROM todos
    WHERE userID={}
    '''.format(u)
    # execute
    try:
        rows = curs.execute(st)
    except Exception as err:
        print('There was a problem:{}'.format(err))
    for item in rows:
        if item[3] == 1:
            phrase = ''
        else:
            phrase ='not'
        print('Item {} (user {}) title:{} is {} completed'
            .format(item[1], item[0], item[2], phrase))
    conn.close() # always make sure the connection is closed
    
if __name__ == '__main__':
    main()