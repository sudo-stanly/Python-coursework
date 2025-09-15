

"""

    ! RECURSION

"""

#* Recursion is a common mathematical and programming concept. It means that function calls itself.
#* This has the benefit of meaning that you can loop though data to reach to a result.

#* The developer should be very careful with recursion as it can be quite easily slip into writing a function
#* which never terminates, or one that uses excess amounts of memory or processor power. However, when written
#* correctly recursion can be a very efficient and mathematically-elegant approach to programming.

#* In this example, ti_recursion() is a function that we have defined to call itself ("recurse"). We use the k
#* variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is
#* not greater than 0 (i.e when it is 0).

#* To a new developer it can take some time to work out how exactly this works, best way to find out is by testing
#* and modifying it.

def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("Recursion Example Results:")
tri_recursion(6)

    #! understanding the recursion
    #* we have a value or 6 passed to the argument
    #* we have a condition if k is > 0 which is true, else result = 0
    #* inside the true statement we have result = k + tri_recursion(k - 1)
    #! which is... result = 6 + tri_recursion(6 - 1)
    #* -> result = 6 + tri_recursion(5)
    
    #! result = 5 + tri_recursion(5 - 1)
        #* -> result = 5 + tri_recursion(4)
        
     #! result = 4 + tri_recursion(4 - 1)
        #* -> result = 4 + tri_recursion(3)
        
    #! result = 3 + tri_recursion(3 - 1)
        #* -> result = 3 + tri_recursion(2)
        
    #! result = 2 + tri_recursion(2 - 1)
        #* -> result = 2 + tri_recursion(1)
        
    #! result = 1 + tri_recursion(1 - 1)
        #* -> result = 1 + tri_recursion(0)
        
    #* k becomes k == 0, result becomes 0 and recursion stops.
    
    #! now to solve them backwards
    #* recurse (0) = 0
    #* recurse (1) = 1 + 0 = 1 -> prints 1
    #* recurse (2) = 2 + 1 = 1 -> prints 3
    #* recurse (3) = 3 + 3 = 6 -> prints 6
    #* recurse (4) = 4 + 6 = 10 -> prints 10
    #* recurse (5) = 5 + 10 = 15 -> prints 15
    #* recurse (6) = 6 + 15 = 21 -> prints 21