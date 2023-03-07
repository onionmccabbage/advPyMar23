import json # the json library is part or Python

# here the JSON library will take json text and convert to Python structures
data = json.load(open('todos.json', 'r'))

# if we need the data as JSON...
data_j = json.dumps(data) # we now have a string of text

# we should now have the entire structure imported
print(data[0], type(data[0]))
print(data_j, type(data_j))