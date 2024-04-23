# Make a function which calculates 
# 'a' raised to the power 'b' using recursion
a = int(input("Enter the number: "))
b = int(input("Enter the power: "))

def a_power_b(a,b):
    if b == 0:
        return 1
    ans = a * a_power_b(a,b-1)
    return ans

result = a_power_b(a,b)
print(result)