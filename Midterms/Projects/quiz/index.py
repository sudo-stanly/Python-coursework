

# text = "python programming"
# print(text[0:6])


def greet(name="Guest"):
    pass


my_list = [] #mutable
my_tuple = () #immutable


my_list = [1, 2, 3, 4, 5]
print(my_list[-1::])

my_set = set({1, 2, 3})
my_set.add(4)
print(my_set)

name = "aragon"
word = "Hello," + name
print(word)




import json

data = {"name":"alice", "age":25}
JSON = json.dumps(data)


# no duplicates
empty_set = set({1, 1, 5, 5, 4})
print(empty_set)

# duplicates
empty_tuple = (1, 2, 3, 4, 4, 4)
print(empty_tuple)

empty_list = [1, 2, 2, 3]
print(empty_list)





PARSE = json.loads(JSON)
# print(f"PARSE is a type of : {type(PARSE)}")





my_list.append("apple")
print(my_list)




TUPLE = (10, 20, 30)
# print(TUPLE)