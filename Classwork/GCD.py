# Program to claculate the greatest common divisor of two numbers

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    print(a)

a=int(input())
b=int(input())
gcd(a,b)