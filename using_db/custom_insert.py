import db_util as db

def customInsertDB():
    '''enter sanitized data into the database'''
    invalid_name  = True
    invalid_count = True
    invalid_cost  = True
    while invalid_name:
        creature_name = input('Creature Name? ')
        if len(creature_name) > 0:
            invalid_name = False
    # validate the count int >0
    while invalid_count:
        # EVERY input is ALWAYS a string. So cast to a float then an int
        count = int(float(input('How many? ')))
        if count >=0:
            invalid_count = False
    # validate the cost float >0
    while invalid_cost:
        cost = float(input('Cost? '))
        if cost >=0:
            invalid_cost = False
    st = '''
    INSERT INTO zoo
    VALUES (?,?,?)
    '''
    try:
        db.curs.execute(st, (creature_name, count, cost))
        db.conn.commit()
        db.conn.close()
    except Exception as err:
        print(err)

if __name__ == '__main__':
    customInsertDB()