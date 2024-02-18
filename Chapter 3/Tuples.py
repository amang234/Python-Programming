# Creating A Tuple
Color = ("Blue","Green","Red","Pink")

# Creating A tuple with a single element
fruit = ("Apple",)
fruits = tuple("Apple")

# Check Type
print(type(Color))
print(type(fruit))
print(type(fruits))

# Check Length
print(len(fruit))
print(len(Color))

# Accessing items in Tuples
# Indexing
print(Color[1])

# Negative Indexing
print(Color[-2])

# Range of indexing
print(Color[1:3])

# Range of Negative indexing
print(Color[-3:-1])

#Check if an item exists in tuple
if "Green" in Color:
    print("Green is a color")

# Traverse The tuple
for i in Color:
    print(i)

# Concatenate 2 tuples
Colors = ("White","Black")
Color = Color + Colors
print(Color)

# Unpacking a Tuple
Color1,Color2,Color3,Color4,Color5,Color6 = Color
print(Color1,Color2,Color3,Color4,Color5,Color6)