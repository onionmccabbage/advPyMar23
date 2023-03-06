# for most purposes th SQL is very similar across different Database implementations
import sqlite3

def readDB():
    ''' read back from the database '''
    conn = sqlite3.connect('mydb')
    curs = conn.cursor()
    # while SELECT * is allowed, SELECT n, m, p is preferrable - more obvious
    # SELECT will return members IN ORDER of SELECTION
    st = '''
    SELECT count, cost, creature FROM zoo
    '''
    try:
        curs.execute(st)
        conn.commit()
        # here we can use the cursor to access any returned data
        rows = curs.fetchall()
    except Exception as err:
        print(err)
    finally:
        conn.close()
    # decide what to return
    animal_l = []
    for animal in rows: # iterate over the rows of returned data
        # remember - we asked for count then cost the ncreature in that order
        animal_l.append('we have {0} {2} each costing {1:0.2f}'.format(animal[0], animal[1], animal[2]))
    return animal_l # we must return the completed list

if __name__ == '__main__':
    result = readDB()
    print(result)