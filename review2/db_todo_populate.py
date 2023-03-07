import sqlite3
import json

def main():
    # read in some JSON from a text file
    fin = open('review2/todos.json', 'rt') # if it's in some other folder
    todos_j = fin.read() # we now have some JSON
    todos_l = json.loads(todos_j) # 'loads' is load-string

    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    # iterate over our structure
    # use '?' as a placeholder in SQL statements
    st = '''
    INSERT INTO todos
    VALUES (?, ?, ?, ?)
    '''
    for item in todos_l:
        try:
            curs.execute(st, (item['userId'], item['id'],item['title'], item['completed']))
            conn.commit()
        except Exception as err:
            print('There was a problem:{}'.format(err))
        finally:
            pass
    # when done, we need to close our connection    
    conn.close() # always make sure the connection is closed

if __name__ == '__main__':
    main()