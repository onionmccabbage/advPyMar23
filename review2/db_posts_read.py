import sqlite3

def main():
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    st = '''
    SELECT userID, id, title, body FROM posts
    '''
    # execute
    try:
        curs.execute(st)
        rows = curs.fetchall()
    except Exception as err:
        print('There was a problem:{}'.format(err))
    finally:
        conn.close() # always make sure the connection is closed

    # we can explore the 'rows'
    for item in rows:
        print('Post {1} (user {0}) title: {2}\n{3}\n'
            .format(item[0], item[1], item[2], item[3]))

if __name__ == '__main__':
    main()