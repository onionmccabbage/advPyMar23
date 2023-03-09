import time
import random
from threading import Thread
import requests

# declare a class which inherits from Thread
class MyThread(Thread):
    ''' we override the 'run' method of the thread access class'''
    def __init__(self, name):
        Thread.__init__(self) # always a good idea to call the initialiser of the parent class
        self.name = name
    def run(self):
        ''' this method will be called when we start an instance of this class as a thread'''
        for i in range(0,50):
            # time.sleep(random.random()*0.1)
            # http requests are asynchronous - we cannot tel how long they might take
            response = requests.get(f'https://jsonplaceholder.typicode.com/photos/{i}')
            response_dict = response.json()
            print(f'{response_dict}')

def main():
    m1 = MyThread('m1')
    m2 = MyThread('m2')
    m3 = MyThread('m3')
    m1.start() # this invokes the 'run' method
    m2.start()
    m3.start()
    m1.join() # we will wait for the threads to re-join this main thread
    m2.join()
    m3.join()
    print('all done')

if __name__ == '__main__':
    main()
