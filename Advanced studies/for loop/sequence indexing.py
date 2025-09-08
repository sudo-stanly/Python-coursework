
"""

    ! sequence indexing

"""

myList = ["apple", "orange", "banana"]
# for x in myList:
#     print(x)
#* this prints all the elements


#! using range() and len directly
# for x in range(len(myList)):
#     print(myList[x])
    
#     if myList[x] == "orange":
#         print("Hello world")
#         break

"""

    * hmmm.. dictionary-

"""

myObj = { "name" : "John Doe", "age" : 23 }
for key, value in myObj.items():
    # print(key, value)
    print(f"{key} : {value}")