import sqlite3 # built in database that comes with Python

def main():
    conn = sqlite3.connect('my_db') # create the database if not exist
    curs = conn.cursor()
  
    st = '''
    DELETE from posts
    '''
    curs.execute(st)
    conn.commit() 
    conn.close()

if __name__ == '__main__':
    main()