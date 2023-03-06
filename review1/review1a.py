from my_decorators import show_args

def root(x):
    return x**0.5 # anything to the power of 0.5 is the square root

def mapRoots(start, number):
    '''
    Return the square root of integers between min and max
    '''
    print('Using Map')
    # roots = map(lambda x: x**0.5, range(start,number+1))
    roots = list( map(root, range(start,number+1)) )
    print(roots)

if __name__ == '__main__':
    number = 0
    # vaidate that a positive integer has been entered
    while number<1:
        number = int(float(input('Enter number : ')))
    start = 0
    mapRoots(start, number)