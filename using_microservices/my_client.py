import socket
import sys # we will inject sys.argv parameters

def microclient():
    '''this is an http client'''
    # same arguments for compatibility
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874)
    sock.connect( param_t )
    # send a message to the server
    if len(sys.argv) > 1:
        msg = ' '.join(sys.argv[1:]) # ignore sys.argv[0]
    else:
        msg = 'default message'
    sock.send( f'{msg}'.encode() ) # .encode will ensure the data is http compliant

if __name__ == '__main__':
    microclient()