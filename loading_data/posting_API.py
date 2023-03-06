import requests # we can make get, post, put, update, delete calls

def makePost():
    url = 'https://httpbin.org/post' # a useful dummy API
    # the POST method requires a payload
    payload = {'item':'pencil', 'status':'sharp', 'cost':3.99}
    # also a good idea to populate a 'header' object
    h = {'Content-Type':'application/json; charset=utf-8' }
    try:
        response = requests.post(url, json=payload, headers=h)
        return response.text # this particular API will respond with text
    except Exception as err:
        return (f'Something went wrong: {err}')

if __name__ == '__main__':
    r = makePost()
    print(r)