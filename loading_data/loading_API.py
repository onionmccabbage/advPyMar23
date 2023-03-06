# historically the 'urllib' was used
# these days we use the 'requests' library
import requests # may need to pip isntall requests
import sys # we will use this to spot any system argument variables
import argparse # a useful tool for dealing with sys.argv values

def makeCall(cat='users', id=1): # some sensible defaults
    '''retrieve some data from an APPI end-point'''
    url = f'https://jsonplaceholder.typicode.com'
    # url = f'https://jsonplaceholder.typicode.com/{cat}/{id}'
    # when making API calls we really should use try...except
    try:
        # response = requests.get('https://nonsuch.ie') # 
        response = requests.get(f'{url}/{cat}/{id}') # this will make a 'get' request to the API
        # we can strip out the data from the response object
        # this next line will populate a dictionary from the json values
        response_j = response.json() # we KNOW this API will return json
        # response_t = response.text() # 
        # response_x = response.xml() # 
        # response_h = response.html() # 
        return response_j
    except Exception as err:
        print(f'There was a problem: {err}') # or log to a file
    finally:
        pass # remember - the finally block will ALWAYS run
        # return 'this code always runs'

if __name__ == '__main__':
    # show any system argument variables
    # NB sys.argv[0] is ALWAYS the name of the module being run
    print(sys.argv) # a list of any passed-in arguments
    r = ''
    # make use of any passed-in system argument variabls
    if len(sys.argv) > 1: # we ignore sys,argv[0] since it is alays the file name
        category = sys.argv[1]
        id       = sys.argv[2]
        print('Calling with sys.argv parameters')
        r = makeCall(category, id)
    else:
        r = makeCall('posts', 3) # override the function default arguments
        
    # r = makeCall() # use the function default arguments
    print(f'response data is: {r}', type(r))