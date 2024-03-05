# Exponential of a number using recursion
def power(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * power(x, n - 1)

x = int(input("Enter the Number: "))
n = int(input("Enter the Power: "))
print(x, "to power", n, "is", power(x, n))
