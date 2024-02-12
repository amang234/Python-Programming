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