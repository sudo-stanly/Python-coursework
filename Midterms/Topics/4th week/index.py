import json

json_string = '''
    {
        "student":[
            {
                "id":1,
                "name":"Linus Torvalds",
                "age": 55
            },
            {
                "id":2,
                "name":"Van Rossum",
                "age": 39
            }
        ]
    }
'''
#! JSON to Python
data = json.loads(json_string) # parse
print(data) # prints as a dict
print(data["student"]) # key
print(data["student"][0]) # access index





# read and writing and generating a json file

# read
with open('example.json', 'r') as f:
    data_2 = json.load(f)
print(data_2)

# write
with open('example_2.json', 'w') as f:
    json.dump(data_2, f)