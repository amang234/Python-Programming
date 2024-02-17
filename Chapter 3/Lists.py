fruits = ["apple","Mango","Banana"]
print(fruits) #print a list
print(type(fruits)) #print type of list
print(len(fruits)) #Print length of list

# Check whether elements there in the list
if "Banana" in fruits:
    print(True)
if "Kiwi" not in fruits:
    print(True)

# Accessing Items in a list
# Indexing
print(fruits[1])

# Negative Indexing
print(fruits[-2])

# Range of indexing
print(fruits[1:3])

# Range of Negative indexing
print(fruits[-3:-1])

# Adding elements to the list
# Append()
fruits.append("Cherry")
print(fruits)
# Insert()
fruits.insert(2,"Pear")
print(fruits)
# Extend()
fruits2 = ["Watermelon","Papaya"]
fruits.extend(fruits2)
print(fruits)

# Removing Elements
# Remove()
fruits.remove("apple")
print(fruits)
# Pop()
fruits.pop()
print(fruits)
fruits.pop(3)
print(fruits)

# Changing items
# At an index
fruits[1]="Apple"
print(fruits)
fruits[1:3]=["Apple","Kiwi","Orange"]
print(fruits)

# Sorting a list
# Ascending order
fruits.sort()
print(fruits)
# Descending order
fruits.sort(reverse=True)
print(fruits)

fruits.reverse()
print(fruits)
