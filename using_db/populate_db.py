import sqlite3

# inject a single value into the DB
def writeSingle():
    '''write a single creature into the DB'''
    conn = sqlite3.connect('mydb')
    curs = conn.cursor()
    st = '''
    INSERT INTO zoo
    VALUES ('Penguin', 256, 0.62)
    '''
    try:
        curs.execute(st)
        conn.commit()
    except Exception as err:
        print(err)
    finally:
        conn.close() # tidy up



# inject a colection of values into the DB


if __name__ == '__main__':
    writeSingle()