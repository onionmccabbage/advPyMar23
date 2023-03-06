from my_decorators import show_args

def is_square(number):
    '''
    determine if a value is a square number
    '''
    if type(number) == int and number > -1:
        root = number**0.5
        check = int(number**0.5)
        return root == check
    else:
        return False 

@show_args
def filterSquares(start, stop):
    '''
    Use the 'is_square' method to filter just square numbers 
    '''
    numbers_sq = list(filter(is_square, range(start, stop+1)))
    for n in numbers_sq:
        print(n)

if __name__ == '__main__':
    filterSquares(-100, 100)
    