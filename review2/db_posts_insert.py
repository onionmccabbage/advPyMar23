import sqlite3
import json

def main():
    # ask for some new 'post' values
    userId = int(float(input('Which userId? ')))
    # the post ID must not be user-definable
    title  = input('What is the title of the post? ')
    body   = input('What is the body of the post? ')

    conn = sqlite3.connect('my_db')
    curs = conn.cursor()

    # find the next id
    st_count_posts = 'SELECT COUNT(*) FROM posts'
    st_num = 'SELECT MAX(id) FROM POSTS'
    num_posts = curs.execute(st_count_posts).fetchall()[0][0]
    print('There are currently {} posts'.format(num_posts))

    st = '''
    INSERT INTO posts
    VALUES (?, ?, ?, ?)
    '''
    try:
        curs.execute(st, (userId, num_posts+1, title, body))
        conn.commit()
    except Exception as err:
        print('There was a problem:{}'.format(err))
    finally:
        pass
    # when done, we need to close our connection    
    conn.close() # always make sure the connection is closed

if __name__ == '__main__':
    main()