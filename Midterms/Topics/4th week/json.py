
#! python json


"""
    JSON is a syntax for storing and exchanging data.
    JSON is text, written with JavaScript object notation.
"""
#* import json

#* Parse JSON - Convert from JSON to Python
# -if you have a JSON string, you can parse it using the json.loads() method.

#* the result will be a python dictionary

#! example: convert from JSON to Python:
import json

# some json
x = {"name":"john", "age":30, "city":"Ney York"}

# parse x:
# y = json.loads(x)

# the result is a Python dictionary:
# print(y["age"])

print(json.dump(x))
