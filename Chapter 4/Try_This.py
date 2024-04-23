# Write a Python function to calculate the factorial of a number
# (a non-negative integer)
# The function accepts the number as an argument.

def factorial(n):
    ans=1
    if n==0:
        ans = 1
    else:
        for i in range(1,n+1):
            ans *= i
    return ans

n = int(input("Enter the number"))
result = factorial(n)
print("The Factorial for the number is " , result)