# Creating a Dictionary
Registration_No = {"Aman":11052,"Harsh":11058,"Mohit":11110,"Saksham":11106}

print(Registration_No)

# Checking Data Type
print(type(Registration_No))

# Checking length
print(len(Registration_No))

# Accessing Elements from the dictionary
print(Registration_No["Harsh"])
print(Registration_No.get("Harsh"))

# print all keys
print(Registration_No.keys())

# Update Values 
Registration_No["Aman"] = 11058
Registration_No["Harsh"] = 11052
print(Registration_No)

# Add elements to the dictionary
Registration_No["Abhinandan"] = 11118
print(Registration_No)

# Add more sequence
Another_Registration_No = {"Aditya":10231,"Shashwat":11378,"Vishu":10378}
print(Another_Registration_No)

Registration_No.update(Another_Registration_No)
print(Registration_No)

# Remove elements from the dictionary
Registration_No.pop("Aditya")
print(Registration_No)

# Remove the last item from the dictionary
Registration_No.popitem()
print(Registration_No)

# # Clear the dictionary
# Registration_No.clear()
# print(Registration_No)

# Printing All values of dictionary
for x in Registration_No:
    print(x)

for x in Registration_No:
    print(Registration_No[x])

for x in Registration_No.items():
    print(x)

for x,y in Registration_No.items():
    print(x,y)

Dinner = {
    "Non Veg" : {
        "Aman" : 11058,
        "Shashwat" : 11378,
        "Aditya" : 10231,
        "Vishu" : 10378
    },
    "Veg" : {
        "Abhi" : 11118,
        "Mohit" : 11110,
        "Harsh" : 11052,
        "Saksham" : 11106
    }
}
print(Dinner)
print(Dinner["Non Veg"]["Aman"])

