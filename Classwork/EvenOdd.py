#Check if a Number is Even or Odd using Bitwise AND
def is_even(num):
    if num & 1 == 0:
        return True
    else:
        return False

num1 = int(input("Enter the number: "))
if is_even(num1):
    print(num1, "is even")
else:
    print(num1, "is odd")
