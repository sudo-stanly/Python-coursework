# list, set , tuple: these are called collections

my_list = []
my_set = set()
my_tuple = ()


# empty collections
empty_list = []
empty_set = set()
empty_tuple = ()

# to add elements/members
#collection .append(value_to_insert)
# empty_list.append(1)
# print(empty_list)

#! doing it this way is not allowed: collection.append(1, 2, 3, 4, 5) -> this will give an error
#* to add muliple elements: use 'extend' collection.extend([1, 2, 3, 4, 5])
# extend can be used to empty collection
# example if collection has elements, the extend can add more elements inside
this_list = [1, 2, 3]
this_list.extend([1, 2, 3])
# print(this_list)

#another way is adding an extended list with another list
empty_list.extend([1, 2, 3, 4, 5])
empty_list = empty_list + [6, 7, 8, 9]
# print(empty_list)

#another way is add() function for set
empty_set.add(2)
empty_set = empty_set.union({2, 3, 4, 5, 6, 7, 8, 9})
# print(empty_set)

#for tuple, since teres only count and index, do it in this way.
#! empty_tuple = empty_tuple + (1, 2, 3) #tuple must only be string
empty_tuple = empty_tuple + (1, 2, 3, 4, 5)

# whole_collection = empty_list, empty_set, empty_tuple
# print(whole_collection)
#or print by for loop
# for elements in whole_collection:
#     print(f"Type {type(elements)} : {elements}")

#removing elements in a collection
#example we want to remove 6-9
empty_list.remove(6) #remove is only available for list and set
empty_list.remove(7)
empty_list.remove(8)
empty_list.remove(9)

empty_set.remove(6)
empty_set.remove(7)
empty_set.remove(8)
empty_set.remove(9)

#removing elements in a tuple
empty_tuple = empty_tuple[:2] + empty_tuple[3:]

whole_collection = empty_list, empty_set, empty_tuple
for elements in whole_collection:
    print(f"Type {type(elements)} : {elements}")
    
    
#! assignment
#* create a simple grocery list using one of the collection discussed. It must accept an input from user.
#* User must be able to add and remove an item from the list.