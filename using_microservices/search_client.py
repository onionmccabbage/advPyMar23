import socket
import sys # we will inject sys.argv parameters
def connex():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874)
    sock.connect( param_t )
    return sock

def microclient():
    '''this is an http client'''
    # same arguments for compatibility
    # we need a run-loop
    while True:
        sock = connex()
        # ask the user for ONE letter (or quit)
        search_term = input('What are you looking for? ')
        if search_term == 'quit':
            sock.close()
            break
        else:
            # send a message to the server
            sock.send( f'{search_term}'.encode() ) # .encode will ensure the data is http compliant
            # handle any response from the server
            response = sock.recv(1024)
            print(f'Received suggestions: {response}')
            sock.close()

if __name__ == '__main__':
    microclient()