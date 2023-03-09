# we can pass events fro mthe main thread to a child thread
from threading import Thread
from threading import Event
import time

event = Event()

class MyClass():
    def __call__(self, name):
        global event # we now have access to the global event object
        print(f'{name} is waiting for a thread event...')
        event.wait() # this thread will go no further until the thread event is received
        print(f'{name} has received the event and is continuing execution')
        time.sleep(3)
        print(f'{name} will send a thread event signal back to the maint thread')
        event.set()

if __name__ =='__main__':
    m1 = MyClass()
    t1 = Thread(target=m1, args=('t1',))
    t1.start()
    # next we make the main thread sleep for a while
    time.sleep(5)
    event.set() # here we make hte event occur, so any thread waiting will receive this signal
    event.wait()
    print('main thread continues after the child thread sends an event signal')
