#Marks Ria
Eng_marks = int(input("Enter the English Marks: "))
Maths_marks = int(input("Enter the Maths Marks: "))

# If both are more than 80, print A grade
if Eng_marks >= 80 and Maths_marks >= 80:
    print("A grade")
elif Eng_marks >= 80 or Maths_marks >= 80:
    print("B grade")
else:
    print("C grade")

# Take positive integer input 
# Tell if it is a four digit number or not.
Number = int(input("Enter The Number: "))
if Number >=1000 and Number <= 9999:
    print("It is a four digit number")
else:
    print("It is not a four digit number")

# Take 3 positive integer input and print the greatest of them
num1 = int(input("Enter the Number 1"))
num2 = int(input("Enter the Number 2"))
num3 = int(input("Enter the Number 3"))

if num1>num2 and num1>num3:
    print("The greatest number is",num1)
elif num2>num1 and num2>num3:
    print("The greatest number is",num2)
else:
    print("The greatest number is",num3)
