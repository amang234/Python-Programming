#Swap Two Numbers
num1 = int(input("Enter the Number 1: "))
num2 = int(input("Enter the Number 2: "))

print("Before swapping:", num1, num2)

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print("After swapping:", num1, num2)