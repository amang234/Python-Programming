input_Tuple = (1,2,3,4,5,6)

list = []

# Adding reversed values in the list
for x in reversed(input_Tuple):
    list.append(x)

# Type casting
output_Tuple = tuple(list)
print(output_Tuple)