# we are going to use HTTP
# so we must concern ourselves with port number,
# IP addresses and even data-transfer object type

import socket

def microserver():
    '''This service will simply echo back any requests'''
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    param_t = ('localhost', 9874) # server IP address and port
    server.bind(param_t)
    # begin listening for clients
    server.listen(4) # we will handle up to 4 concurrent requests
    print(f'Server is listening on {param_t[0]} port {param_t[1]}')
    # we need to keep our server running. Typically this is called a run-loop
    while True:
        # when a request is made, we need to handle it
        (client, addr) = server.accept()
        print(f'Server received a request from {client} at {addr}')
        # if the client request was 'quit' then we will stop the server
        buf = client.recv(1024) # we receive a buffer-full from the client
        print(f'Server received {buf}') # print will covert the bytes into a string
        if buf == b'quit':
            server.close() # tidy up
            break

if __name__ == '__main__':
    # invoke our microservice
    microserver()


