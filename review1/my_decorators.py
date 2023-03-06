def show_args(func):
    def my_fn(*args, **kwargs):
        print('Running a function called {}'.format(func.__name__))
        print('Positional arguments are {}'.format(args))
        print('Keyword arguments are {}'.format(kwargs))
        return func(*args, **kwargs)
    return my_fn

def show_intrinsics(func):
    '''reveal some of the instrinsics for the function'''
    def inner_func(*args, **kwargs):
        print('Function name is {}'.format(func.__name__))
        print('Docstring is {}'.format(func.__doc__))
        print('in module {}'.format(func.__module__))
        return func(*args, **kwargs)
    return inner_func