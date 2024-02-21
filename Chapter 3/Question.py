# Given a string and a number 
# We need to mirror the characters from the 
# N-th position up to the length of the string in alphabetical order. 
# In mirror operation, we change 'a' to 'z', 'b' to 'y' and so on.
# Input: N = 3
#        paradox
# Output : paizwlc
# Input: N = 6
#        pneumonia 
# Output : pneumlmrz
String = input("Enter the string: ")
N = int(input("Enter the N: "))

# Create dictionary for mirror operation
Alphabets = "abcdefghijklmnopqrstuvwxyz"
Reverse_Alphabets = Alphabets[::-1]
dict1 = dict(zip(Alphabets,Reverse_Alphabets))

# Find the part of string on which we need to perform the operation
Prefix = String[0:N-1]
Suffix = String[N-1: ]
# Finding the mirror string
mirror = ""
for i in range(0,len(Suffix)):
    mirror = mirror + dict1[Suffix[i]]

# Creating the final string
Result = Prefix + mirror
print("The resulting string is:",Result)