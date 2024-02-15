# If Else Elif
Num = int(input("Enter the Number: "))

# Take integer input and tell if it is positive or negative
if Num >= 0:
    print("The number", Num,"is positive")
else:
    print("The number", Num,"is Negative")

# Take positive integer input and tell if it is even or odd
if Num % 2 == 0:
    print("The Number is even")
else:
    print("The Number is odd")

# If cost price and selling price of an item is input through the keyboard
# Write a program to determine whether the seller has made profit 
# Or incurred loss or no profit no loss. 
# Also determine how much profit he made or loss he incurred.
    
Cost_Price = int(input("Enter the Cost Price: "))
Selling_Price = int(input("Enter the Selling Price: "))

if Cost_Price - Selling_Price > 0:
    print("There's a loss of", Cost_Price - Selling_Price)
elif Cost_Price - Selling_Price == 0:
    print("No Profit No Loss")
else:
    print("There's a profit of", Selling_Price - Cost_Price)

# Take input percentage of a student and print the Grade according to marks:
# A 81-100 Very Good
# B 61-80 Good
# C 41-60 Average
# D <=40 Fail

Marks = int(input("Enter your Marks: "))

if Marks <= 40:
    print("Fail")
elif Marks <= 60:
    print("Average")
elif Marks <= 80:
    print("Good")
else:
    print("Very Good")