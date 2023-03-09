# we do not need to extend the Thread class - any class can be invoked into a thread

from threading import Thread
import time
import random
import requests

# declare a callable class
class MyClass: # this does NOT inherit from Thread
    def __call__(self, thread_name, cat):
        '''this method can be called to make a new Thread'''
        # remember we should be using try-except for request calls
        r = requests.get(f'https://jsonplaceholder.typicode.com/{cat}')
        r_dict = r.json()
        print(f'{thread_name} retrieved {r_dict}')

def main():
    m1 = MyClass()
    m2 = MyClass()
    m3 = MyClass()
    m4 = MyClass()
    m5 = MyClass()
    # next we will invoke some threads - they will make asynchronous calls to an API
    t1 = Thread(target=m1, kwargs={'thread_name':'t1', 'cat':'users'} ) # kwargs as a dict
    t2 = Thread(target=m2, args=('t2', 'posts')) # positional args as a tuple
    t3 = Thread(target=m3, args=('t3', 'todos'))
    t4 = Thread(target=m4, args=('t4', 'albums'))
    t5 = Thread(target=m5, args=('t5', 'photos'))
    my_threads = (t1, t2, t3, t4, t5) # a tuple (or a List)
    for t in my_threads: # this is a tidy way to handle multiple threads
        t.start()
    # always start the threads before join 
    # otherwise the 'start' must wait for prev thread to join
    for t in my_threads:
        t.join() # remember - the main thread will now wait for each thread to (re)join

if __name__ == '__main__':
    main()