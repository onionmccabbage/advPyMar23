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


if __name__ == '__main__':
    # print( showSquare(3) ) # 9
    doctest.testmod(verbose=True)