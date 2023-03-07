# here we carry out the generic DB steps we need
import sqlite3

conn = sqlite3.connect('mydb')
curs = conn.cursor()