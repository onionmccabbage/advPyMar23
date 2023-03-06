# there are many things built-in to how Python works
# These are known as 'instrinsics'
# we have met __name__  -all intrinsicts have leading and trailing double-underscore

class TopLevel():
    def __init__(self):
        pass # do nothing

class Derived(TopLevel):
    ''' this class is derived from the 'TopLevel' class '''
    def __init__(self):
        super().__init__() # call the initializer of the parent class
    def __str__(self):
        return 'instance of the derived class'

if __name__ == '__main__':
    t = TopLevel()
    d = Derived()
    print(t, d)
    # we can explore some intrinsic properties
    print(f'Class name is {Derived.__name__}')
    print(f'Class docstring is {Derived.__doc__}')
    print(f'Class dictionary is {Derived.__dict__}') # all memers of the class
    print(f'Class bases are {Derived.__bases__}') # everything in the inheritance chain