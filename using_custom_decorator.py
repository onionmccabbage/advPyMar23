# the '@' sign is used in Python to apply a 'decorator'
def show_Args(func):
    ''' this function will be used to decorate ANY other function
    Its purpose is to reveal all the incoming positional arguments and keyword arguments'''
    # *args will always gather together the positional arguments into a tuple
    # **kwargs will always gather together the keyword arguments into a dictionary
    def new_fn(*args, **kwargs):
        print(f'Running a function called {func.__name__}')
        print(f'The positional arguments are {args}')
        print(f'The keyword arguments are {kwargs}')
        # we should also execute the passed-in function
        return func(*args, **kwargs) # ALL positional args MUST precede any keyword args
    return new_fn # return our new function

# a trivial function to be decorated
@show_Args # here we apply our function as a decorator
def add_integers(a, b):
    '''return the sum of two integers'''
    return int(a)+int(b)

if __name__=='__main__':
    result = add_integers(3, 4) # here we pass positional arguments
    result2 = add_integers(a=3, b=4) # here we pass keyword arguments
    result3 = add_integers(3, b=4) # here we pass keyword arguments
    print(result)