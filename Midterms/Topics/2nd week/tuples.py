
#! How to remove elements in tuple, list method:
movies = ("Inception", "Interstellar", "Tenet", "Dunkirk", "Memento")

# Convert the tuple to a list
movies_list = list(movies)

# Remove specific items
# movies_list.remove("Tenet")
# movies_list.remove("Dunkirk")
list_to_remove = ["Tenet", "Dunkirk"]
for list in list_to_remove:
    movies_list.remove(list)

# Convert the list back to a tuple
movies = tuple(movies_list)

print(movies)