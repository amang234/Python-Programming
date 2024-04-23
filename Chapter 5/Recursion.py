def factorial(n):
    
    # Base case
    if n == 1:
        return 1
    
    # recursive Case
    ans = n * factorial(n-1)
    return ans
n = int(input("Enter the value: "))
result = factorial(n)
print("The factorial is ",result)