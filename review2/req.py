import sqlite3
import requests
conn = sqlite3.connect('my_db')
curs = conn.cursor()
st = '''
INSERT INTO todos
VALUES (?, ?, ?, ?)
'''
def populateDB():
    url = 'https://jsonplaceholder.typicode.com/todos' # this API always returns JSON
    try:
        response = requests.get(url)
        data = response.json() # this returns 200 data members (0-199)
        # iterate over the data to populate the db
        for item in data: # here we insert each row into the DB - could be more efficient
            try:
                curs.execute(st, (item['userId'], item['id'], item['title'], item['completed']))
                conn.commit()
            except Exception as err:
                print('There was a database problem:{}'.format(err))
    except Exception as err:
        print('There was a request problem:{}'.format(err))
    conn.close() # always make sure the connection is closed

if __name__ == '__main__':
    populateDB()