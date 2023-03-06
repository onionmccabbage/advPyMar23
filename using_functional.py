# here we explore map, filter, reduce
from functools import reduce
# these are pure functions - 
# they will return entirely predicable results given known inputs

def squareIt(x):
    '''return the square of the argument'''
    return x*x # or x**2

def addThem(x,y):
    '''return the sum of the arguments'''
    return x+y

def isOdd(n):
    '''return True or False depending if the argument is odd or not'''
    return n%2 != 0 # True if odd, False if even

if __name__ == '__main__':
    # we need a collection of all the square numbers in a range
    # here we create 'map' object
    squares = ( map(squareIt, range(1, 12)) ) # start at 1, stop before 12
    # we can iteratively pick members from our map object
    print(f'the next square result is { squares.__next__() }') # yield the next available value
    print(f'the next square result is { squares.__next__() }') # 4
    print(f'the next square result is { squares.__next__() }') # 9
    # we can persist the values in a collection
    squares_list = list(squares) # cast into a list - now all the values persist in memory
    # print( list(squares)) # nothing - the map object has already been exhausted
    print(squares_list, type(squares_list))

    # we can also use 'filter' to return a generator-like collection
    odds = ( filter(isOdd, range(1, 28)) )
    print( odds, type(odds) )
    print( odds.__next__() ) # yields 1
    print( odds.__next__() ) # yields 3
    # we can gather them into a collection
    odds_tup = tuple(odds) # just the remaining values
    print(odds_tup)

    # 'reduce' will recursively apply a function
    # so it gets a value, then injects THAT value to the function, 
    # then again injects THAT returned value to the function
    r = reduce( addThem, odds_tup ) # this will add all the valuesd from the tuple
    print(r, type(r))