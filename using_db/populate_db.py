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



# inject a collection of values into the DB
def populateDB():
    '''pass parameters into the DB for each new creeature'''
    # NB usually we would access this data from an API, user input, file, sensors etc.
    creatures_t = ( # a tuple of dictionaries
        {'creature':'Albatros', 'count':1,     'cost':120.99},
        {'creature':'Bear',     'count':1,     'cost':323.99},
        {'creature':'Carp',     'count':1,     'cost':87.99},
        {'creature':'Deer',     'count':1,     'cost':12.99},
        {'creature':'Elk',      'count':1,     'cost':73.99}
    )
    # 'conn' is not the database, it is a data access object (DAO)
    conn = sqlite3.connect('mydb')
    curs = conn.cursor()
    # for security we often use parameters in our SQL statements
    #the '?' stands for a data parameter we will inject
    st = '''
    INSERT INTO zoo
    VALUES (?, ?, ?)
    '''
    for item in creatures_t:
        try:
            # we should always check the data members are of the correct data type
            if type(item['creature'])==str and item['creature'] != '':
                n = item['creature'] # all good
            else:
                raise Exception('Name must be a non-empty string')
            if type(item['count'])==int and item['count'] >=0:
                c = item['count']
            else:
                raise Exception('Count must be zero or greater integer')
            if type(item['cost'])==float and item['cost'] >=0:
                co = item['cost']
            else:
                raise Exception('Cost must be zero or greater float')
            # if there were no exceptions, we now have n, c and co
            # we use these sanitized values in our SQL statement
            curs.execute(st, (n, c, co)) # the members n, c and co will replace the '?'
            conn.commit() # this is where any changes are made persistent
        except Exception as err:
            print(err)
    conn.close() # tidy up after the 'for' loop has completed

if __name__ == '__main__':
    populateDB()
    # writeSingle()