import sqlite3
import json

def main():
    # read in some JSON from a text file
    fin = open('review2/posts.json', 'rt') # if it's in some other folder
    posts_j = fin.read() # we now have some JSON
    posts_l = json.loads(posts_j) # 'loads' is load-string

    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # iterate over our structure
    # use '?' as a placeholder in SQL statements
    st = '''
    INSERT INTO posts
    VALUES (?, ?, ?, ?)
    '''
    for item in posts_l:
        try:
            curs.execute(st, (item['userId'], item['id'],item['title'], item['body']))
            conn.commit()
        except Exception as err:
            print('There was a problem:{}'.format(err))
        finally:
            pass
    # when done, we need to close our connection    
    conn.close() # always make sure the connection is closed

if __name__ == '__main__':
    main()