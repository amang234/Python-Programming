# Program to claculate the greatest common divisor of two numbers

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))
print("The GCD of", num1, "and", num2, "is", gcd(num1, num2))