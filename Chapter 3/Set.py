# Creating a set
Names = {"Aman","Abhinandan","Harsh","Shashwat","Arnav"}
# print set
print(Names)
# Check length of sets
print(len(Names))
# Check data type of sets
print(type(Names))

for x in Names:
    print(x)

# Check if an item exists in a set
if "Harsh" in Names:
        print(True)

# Add elements in a set
Names.add("Mohit")
print(Names)

# Add a sequence in a set
Name = {"Vishu","Aditya","Saksham","Arnav"}
Names.update(Name)
print(Names)

# Removing elements from a set
Names.remove("Aditya")
Names.discard("Rishiraj") # This function will not throw an error if the value is not present in the set
print(Names)

# Joining two Sets
print(Names,Name)
name_union = Names.union(Name)
print(name_union)

# Keep only duplicates
name_intersect = Names.intersection(Name)
print(name_intersect)

# Keep all values except duplicates
Names.symmetric_difference_update(Name)
print(Names)

# Only duplicates but updates in a set
Names.intersection_update(Name)
print(Names)
