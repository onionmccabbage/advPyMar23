# threads let us run code concurrently
# all the threads share the ONE isntnace of Python
import time
import random
import timeit
from threading import Thread

# here we emulate a function which will take a variable amount of time
def myfunc(name):
    '''iterate over a range, sleeping for a random time each iteration'''
    for i in range(0, 50): # this will take about 0.25 sec
        time.sleep(random.random()*0.1) # sleep for up to 1/10 second
        print(name, end=", ")

if __name__ == '__main__':
    # remember - this will use ONE processor with MUTLIPLE threads
    start = timeit.default_timer()
    # run the function on several threads (i.e. run them in parallel)
    thread1 = Thread( target=myfunc, args=('t1',) )
    thread1.start() # this gets our new thad running
    thread2 = Thread( target=myfunc, args=('t2',) )
    thread2.start()
    thread3 = Thread( target=myfunc, args=('t3',) )
    thread3.start()
    thread1.join() # this is good practice - tell the thread to rejoin the main thread
    thread2.join()
    thread3.join()

    # we can try running the same thing in sequence...
    # myfunc('f1') # these three functions run on the MAIN thread
    # myfunc('f2') # this line will only run when the previous line has completed
    # myfunc('f3') # we call this 'blocking'
    end = timeit.default_timer() # careful - this time the main thread only!!
    print('', f'total time {end-start}') # 2.5 sec in total (2.5 sec both in parallel)