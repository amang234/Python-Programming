# Make a function which calculates Fibonacci sequence using recursion.

n= int(input("Enter the Number: "))

def FibonacciNumber(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return FibonacciNumber(n-1) + FibonacciNumber(n-2)
    
    
for i in range(1,n+1):
    result = FibonacciNumber(i)
    print(result)
