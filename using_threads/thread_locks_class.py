# here two instances of a class will battle over a shared asset
from threading import Lock
from threading import Thread

# some global assets
lock = Lock()
count1 = 0
count2 = 100

class MyClass:
    def __call__(self, name):
        global lock, count1, count2
        lock.acquire() # this class instance has exclusive access to assets via the lock
        for i in range(0, 20): # inside a lock
            count2 += 1
            print(f'{name} set count2 to {count2}')
        lock.release() # let other threads access stuff       
        for i in range(0, 20): # with no lock
            count1 += 1
            print(f'{name} set count1 to {count1}')

def main():
    m1 = MyClass()
    m2 = MyClass()
    t1 = Thread(target=m1, args=('m1',)) # remember the comma makes this a one-member tuple
    t2 = Thread(target=m2, args=('m2',)) 
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()