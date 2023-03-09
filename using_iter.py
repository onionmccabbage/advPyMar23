# iter is a tool to make things iterable using __next__
my_l = [1, 7, 11, 42]
my_iter = iter( my_l ) # it is now an iter object
print(type(my_iter))

# we can now call __next__()

print( my_iter.__next__() ) # 1
print( my_iter.__next__() ) # 7

rev_iter = reversed(my_l) # an iterable of the list in reverse

print( rev_iter.__next__() ) # 42

class Evens: # this is an iterator class ( rather like a generator )
    def __init__(self, limit):
        self.__limit = limit
        self.__val = 0
    # we override __iter__ and __next__
    def __iter__(self):
        return self
    def __next__(self):
        if self.__val > self.__limit:
            raise StopIteration
        else:
            return_val = self.__val
            self.__val += 2 # we need even numbers
        return return_val
    
inst_evens = Evens(12)
print(inst_evens.__next__()) # 0
print(inst_evens.__next__()) # 2
print(inst_evens.__next__()) # 4
print(inst_evens.__next__()) # 6

for i in Evens(1200): # Evens is our own custom iterator
    print(i)