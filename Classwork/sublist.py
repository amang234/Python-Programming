# Check if a sublist is present in a list of lists
lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
sublist = [4, 5, 6]
if sublist in lists:
    print("Sublist", sublist, "is present in the list of lists.")
else:
    print("Sublist", sublist, "is not present in the list of lists.")
