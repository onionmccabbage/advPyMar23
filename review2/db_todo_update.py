import sqlite3

def main():
    conn = sqlite3.connect('my_db')
    curs = conn.cursor()
    invalid = True
    while invalid:
        t = int(float(input('id?')))
        if type(t) == int and t > 0:
            invalid = False
    st = '''
    UPDATE todos
    SET completed = true
    WHERE id IS {}
    '''.format(t) 
    try:
        curs.execute(st)
        conn.commit()
    except Exception as err:
        print('There was a problem:{}'.format(err))
    finally:
        conn.close() # always make sure the connection is closed

if __name__ == '__main__':
    main()