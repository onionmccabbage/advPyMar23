from contextlib import contextmanager
import sys

@contextmanager # we use the context manager to decorate this function
def redirectOutput(new_context):
    '''Send printed output to a different context then restore the default'''
    save_ctx = sys.stdout # stdout is the standard output (the console)
    sys.stdout = new_context # now any print will be directed ot the new conttext
    yield # this will ensure buffered lines all get yielded
    # make sure the original context is restored
    sys.stdout = save_ctx

if __name__ == '__main__':
    with open('mylog.txt', 'a') as fobj:
        with redirectOutput(fobj):
            print('This text will be written to our log file')
    print('This text returns to the original context, i.e. the console')