#example 1: basic slicing
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sliced_list = my_list[2:5]

# slice has 3 parameters but let's start with 2, [ inception : exception ] or [ index : range ]
# for the index we always start with 0, inside the array we have 0-9 numbers.
# the index starts with an element 0, since the sliced list is 2:5, we want our index to start
# at 2 which is 2 in element, our range is 5, the numbering becomes 1 2 3 4 5, in this case 
# the element 4 becomes the 5th range, so the output is [2, 3, 4]

#example 2: start-stop-step
sliced_list = my_list[2:5:2]
# in this example the step parameter is used, that means the index will jump 2 times for the
# next element to output, example we want odd numbers
odd_numbers = my_list[1:10:2]
    # we can also leave the start empty if we start with the first element, the range will
    # depend on where you want it to stop and step.

#example 3: Slicing string
my_string = "Hello, World!"
sliced_string = my_string[7:12] #print "world"
sliced_string = my_string[:12:2] #print "Hlo ol"

print(sliced_string)