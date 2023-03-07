import db_util as db # we would then use db.conn and db.curs
# from db_util import conn, curs # then we just use conn and curs

def custom_readDB():
    '''Ask the user which creature they would like to read from the DB'''
    invalid = True
    while invalid:
        whichCreature = input('Which Creature? ')
        if len(whichCreature) > 0:
            invalid = False
    # we use an SQL 'where' clause
    # NB inside SQL statements, strings MUST be in DOUBLE QUOTES
    st = f'''
    SELECT creature, count, cost
    FROM zoo
    WHERE creature="{whichCreature}"
    '''   
    # careful - suppose someone wrote malicious code - we MUST validate
    # now we execute our statement against our database access object
    try:
        db.curs.execute(st)
        rows = db.curs.fetchall()
    except Exception as err:
        print(err)
    finally:
        db.conn.close()
    # iterate over the returned data (we expect ONE member)
    for animal in rows:
        print(f'We have {animal[1]} {animal[0]} each costing {animal[2]}')





if __name__ == '__main__':
    custom_readDB()
