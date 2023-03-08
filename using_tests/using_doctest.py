# we can write simple tests
import doctest

def showSquare(n):
    '''return the square of n
    >>> showSquare(3)
    9
    >>> showSquare(10)
    100
    '''
    return n*n

def showCubes(a, b):
    '''return the cube of all numbers between a and b
    >>> showCubes(0, 3)
    [0, 1, 8]
    >>> showCubes(0, 101) # doctest:+ELLIPSIS
    [0, 1, 8, ..., 1000000]
    '''
    answers = []
    for i in range(a,b):
        answers.append( i**3 )
    return answers

if __name__ == '__main__':
    # print( showSquare(3) ) # 9
    # print(showCubes(0, 9))
    doctest.testmod(verbose=True)
