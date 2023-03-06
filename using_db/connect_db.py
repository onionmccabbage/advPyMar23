# a database is an external persistent repository for structured data
# There exists a 'database' containing zero or more 'tables'
# Every table is like a spreadsheet - rows of data usually indexed by an id
# the data rows must comply to declared data types

import sqlite3 # this database tool is part of Python

def accessDB():
    ''' this function will make a connection to our database'''
    conn = sqlite3.connect('mydb') # connect or create
    # we need a cursor to work with the database
    curs = conn.cursor()
    # we need some SQL statements. In this case to declare our table structure
    st = '''
    CREATE TABLE zoo 
    (
        creature VARCHAR(32) PRIMARY KEY,
        count INT,
        cost FLOAT
    )
    '''
    # always a good idea to use try...except
    try:
        curs.execute(st) # pass our SQL statement to the databaase via the cursor
        conn.commit() # make any changes persist in the DB
        conn.close() # tidy up, release any resources
    except Exception as err:
        print(err)

if __name__ == '__main__':
    accessDB()



# some other DB conn mechanisms
# see https://wiki.python.org/moin/DatabaseInterfaces
# DB2
# import DB2 # remember to pip isntasll first!!
# conn = DB2.connect(dsn='ibm-DB', uid='analyst', pwd='db2pwd')

# Sybase
# import Sybase
# conn = Sybase.connect('SYBASE', 'username', 'passwd', 'databasename')

# Oracle
# import cx_Oracle
# conn = cx_Oracle.connect('username', 'passwd', 'hostname:port/SID')
# conn2 = cx_Oracle.connect('username/passwd@hostname:portno/SID')
# dsn_tns = cx_Oracle.makedsn('hostname', portno, 'SID')
# conn3 = cx_Oracle.connect('username', 'passwd', dsn_tns)

# MySQL
# import MySQLdb
# conn = MySQLdb.connect(host = "hostname", user = "username",
# passwd = "password", db = "dbname")

# PySQLite
# from pysqlite2 import dbapi2 as sqlite
# conn = sqlite.connect("mydb", connectionproperties)

# ODBC
# import odbc
# conn = odbc. odbc("myDSN/username/password")