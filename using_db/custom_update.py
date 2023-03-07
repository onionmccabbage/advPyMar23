import db_util as db

def custom_update_DB():
    ''' take parameters for name and count, then update the DB'''
    invalid = True
    while invalid:
        whichCreature = input('Which creatue needs updating? ')
        if whichCreature != '':
            invalid = False
    # ask for a new quantity
    qty = int(float(input('What is the new quantity? ')))
    st = f'''
    UPDATE zoo
    SET count = {qty}
    WHERE creature IS "{whichCreature}"
    '''
    try:
        db.curs.execute(st)
        db.conn.commit()
        db.conn.close()
    except Exception as err:
        print(err)
if __name__ == '__main__':
    custom_update_DB()