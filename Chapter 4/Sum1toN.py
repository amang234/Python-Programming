# Writing a function to print the sum of 1 To N
def sum1ToN(n):
    Sum = 0
    for i in range(1,n+1):
        Sum+=i
    return Sum
n = int(input("Enter the number: "))
output = sum1ToN(n)
print("The sum of numbers from 1 to",n,"is",output)

n1 = int(input("Enter the next number: "))
output1 = sum1ToN(n1)
print("The sum of numbers from 1 to",n,"is",output1)