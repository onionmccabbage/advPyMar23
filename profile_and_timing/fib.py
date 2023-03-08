import time # total time to execute
import timeit # only includes time taken by Python - ignores system activity
from functools import reduce

# we can use cprofile to get a good idea of the profile of performance
# To invoke cprofile
#                    -o will force Python to optimize the module
# python -m cProfile -o profile_output fib.py
# we get a record of num calls, total time, time per call etc.


def fib1(n):
    '''return the fibonacci series up to n
    1, 2, 3, 5, 8, 13, 21 ...
    '''
    if n<=1:
        return 1
    else:
        # self-reference this function - we iteratively call the same function
        return ( fib1(n-1)+fib1(n-2) )
# a global variable
n=20 # 40 iterations took about half a minute on my laptop

def fib2(n): # plenty of wvidence suggests this is the more performant approach
    '''return the fibonacci series up to n'''
    seq = (0, 1) # a tuple
    for _ in range(2, n+1):
        seq += ( reduce( lambda a, b: a+b, seq[-2:] ), )
    return seq[n] # return the last member of our tuple

def averageTime():
    global n # we have access  to the global value of n
    num_iterations = 100
    t = 0
    for _ in range(0, num_iterations):
        start = timeit.default_timer()
        fib2(n)
        end=timeit.default_timer()
        t += end-start
    return t/num_iterations # simple average

if __name__ == '__main__':
    s1 = time.time()
    result = fib1(n)
    s2 = time.time()
    print(f'{result} took about  {s2-s1} seconds')
    # ideally take a number of samples then take an average
    # print( f'100 iterations took an average time of {averageTime()}' )
