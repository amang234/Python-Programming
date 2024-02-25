# Write a function to print Hello Aman
def printHello():
    # Body of our function
    print("Hello Aman!!")
printHello()


# Addition using Function
def Add(n1=0,n2=0):
    sum = n1 + n2
    return sum
x = int(input("Enter the Number 1: "))
y = int(input("Enter the Number 2: "))
sum = Add(x,y)
print("The sum of Numbers is",Add(x,y))

# Positional Arguments
print("The sum of Numbers is",Add(4,5))

# Keyword Argument (named argument)
print("The sum of Numbers is",Add(n1=4,n2=5))

# Default Arguments
print("The sum of Numbers is",Add())    

# Arbitrary arguments
def addAllNumbers(*args):
    # args -> Tuple
    sum = 0
    for i in args:
        sum += i
    return sum 
output = addAllNumbers(1,2,3,4,5,8,54,23,97,23)
print("The Sum will be",output)

def studentInfo(**kwargs):
    # kwargs -> Dictionary
    for x,y in kwargs.items():
        print(x,"is",y)
studentInfo(name="Aman",age="21",City="Gurugram")
studentInfo(name="Harsh",age="20",City="Udaipur")