import sqlite3

def readDB():
    ''' read back fro mthe database '''
    conn = sqlite3.connect('mydb')
    curs = conn.cursor()
    st = '''
    SELECT * FROM zoo
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
        animal_l.append('we have {1} {0} each costing {2:0.2f}'.format(animal[0], animal[1], animal[2]))
    return animal_l # we must return the completed list

if __name__ == '__main__':
    result = readDB()
    print(result)