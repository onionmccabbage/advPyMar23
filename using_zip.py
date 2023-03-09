# in Python zip has nothing to do with compression

def main():
    '''here we declare several collections which will be joined using zip'''
    days     = ['Mon', 'Tue', 'Wed', 'Thur', 'Fri'] # only four get 'zipped'
    fruits   = ('banana', 'kiwi', 'orange', 'Durian')
    drinks   = ['coffee', 'tea', 'water', 'lemonade']
    desserts = {'tiramasu', 'ice cream', 'pie', 'cheese board'}
    z = zip(days, fruits, drinks, desserts)
    for day, fruit, drink, dessert in z:
        print(f'On {day} I ate {fruit} with {drink} followed by {dessert}')
    print(f'The zip object contains {list(z)}', type(z)) # when all the members have been used, the zip is exhausted

if __name__ == '__main__':
    main()