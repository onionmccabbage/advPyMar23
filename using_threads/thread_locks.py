# in addition to the GIL we can take control of when threads are permitted to access assets
from threading import Lock
from threading import Thread
import time
import timeit
import random

# we often think in terms of thread 'workers'
# each worker has a job to do
# each worker may need to access a shared asset

# here are some global assets
counter = 0 # this could be a db, a file etc.
lock = Lock() # a shared lock - all threads will make use of this ONE lock

def workerA(): # we will run this code will on its own thread
    global counter # we have access to the shared asset
    # grab the global lock
    lock.acquire() # this function now has exclusive use of the lock - (it is a mutex)
    # typically we would now try to access some shared asset: db, file, api, sensor, bytes ...
    try:
        # with lock: # if we use 'with' the lock will automatically release at the end
        # increment the counter
        while counter < 100:
            counter += 1
            print(f'Worker A increments the counter to {counter}')
    except Exception as err:
        print(f'oh dear {err}')
    finally:
        pass # we might need to tidy up here
        lock.release()

def workerB(): # we will run this code will on its own thread
    global counter # we have access to the shared asset
    # grab the global lock
    lock.acquire() # this function now has exclusive use of the lock - (it is a mutex)
    # typically we would now try to access some shared asset: db, file, api, sensor, bytes ...
    try:
        # with lock: # if we use 'with' the lock will automatically release at the end
        # increment the counter
        while counter > -100:
            counter -= 1
            print(f'Worker B decrements the counter to {counter}')
    except Exception as err:
        print(f'oh dear {err}')
    finally:
        pass # we might need to tidy up here
        lock.release()

def main():
    thread1 = Thread(target=workerA)
    thread2 = Thread(target=workerB)
    thread2.start()
    thread1.start()
    thread1.join()
    thread2.join()

if __name__ == '__main__':
    start = timeit.default_timer()
    main() # inside our function we acquire then release a lock
    end = timeit.default_timer()
    print(f'it took {end-start}')

