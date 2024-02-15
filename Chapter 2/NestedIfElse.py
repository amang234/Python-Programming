# The greatest of the three numbers
n1 = int(input("Enter the number 1: "))
n2 = int(input("Enter the number 2: "))
n3 = int(input("Enter the number 3: "))

if n1 > n2:
    if n1 > n3:
        print("The greatest number is",n1)
    else:
        print("The greatest number is",n3)
else:
    if n2 > n3:
        print("The greatest number is",n2)
    else:
        print("The greatest number is",n3)

# Take positive integer input 
# and tell if it is divisible by 5 or 3 
# but not divisible by 15.
if n1 % 15 == 0:
    print("The number is divisible by 15")
else:
    if n1 % 3 == 0 or n1 % 5 == 0:
        print("The number is not divisible by 15 but divisible by 3 or 5")
    else:
        print("The number is neither divisible by 15 nor divisible by 3 or 5")
