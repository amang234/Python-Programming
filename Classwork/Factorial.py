# Factorial of n
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

n = eval(input("Enter the number to find factorial1"))
print("Factorial of", n, "is", fact(n))
