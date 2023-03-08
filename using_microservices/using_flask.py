# we may need to pip install flask
# python -m pip install flask
from flask import Flask
import requests # we may need this
import json

# we wil explore Flask architecture and create web URL links (known as 'routes')
app = Flask(__name__) # any name will do, but by convention we use the module name
# we then declare one or more routes for our app (each route uses http 'get')
@app.route('/') # this is the root of our website
def root():
    return 'hello and welcome to our Flask application' # or '<html><body><h2>Hello</h2></body></html>'

@app.route('/home') # we can invent any names for our routes
def home():
    content = '''
    <h2>Flask Home Web Page</h2>
    '''
    return content

@app.route('/todos')
def todos():
    data = json.load(open('todos.json', 'r'))
    data_j = json.dumps(data)
    return data_j # we can only send string data

@app.route('/links')
def links():
    content = '''
    <h3>Visit these links</h3>
    <a href='http://localhost:5000'>Top level</a> |
    <a href='http://localhost:5000/home'>Home</a> |
    <a href='http://localhost:5000/todos'>To do list</a>
    '''
    return content




if __name__ == '__main__':
    app.run() # this starts our Flask web server