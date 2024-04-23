n= int(input("Enter The Number: "))

# Sum of 1 to N
def Sum1toN(n):
    if n==1:
        return 1
    ans = n + Sum1toN(n-1)
    return ans

result = Sum1toN(n)
print(result)
