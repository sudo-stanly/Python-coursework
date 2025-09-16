
#* odd or even

def addFunc():
    num1 = int(input("num 1: "))
    num2 = int(input("num 1: "))
    sum = num1 + num2
    return sum

def logFunc():
    resultOE = addFunc()
    if resultOE % 2 == 0:
        print("Sum is even")
    else:
        print("Sum is odd")
logFunc()