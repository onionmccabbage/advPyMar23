import threading
import time

def normalThread():
    '''this function will be called as an ordinary thread'''
    print('starting a normal thread')
    time.sleep(15)
    print('ending a normal thread')

def daemonThread():
    '''this function will be called as a daemon thread'''
    print('starting a daemon thread')
    while True:
        print('heartbeat')
        time.sleep(0.5)
    print('ending a daemon thread')

if __name__ == '__main__':
    n = threading.Thread(target=normalThread)
    d = threading.Thread(target=daemonThread) # , daemon=True
    d.daemon=True

    d.start()
    n.start()

    # no join
