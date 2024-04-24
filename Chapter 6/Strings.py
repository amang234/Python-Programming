# Creating Strings
Name1 = 'Aman Grover'
Name2 = "Ravi Grover"
Name3 = '''Pooja
Grover'''
Name4 = "    Hello World!     "
print(Name1,Name2,Name3)
print(type(Name1))
print(type(Name2))
print(type(Name3))

# Indexing
print(Name1[0])
print(Name1[5])
print(Name1[-1])

# Traversing
# Using For loop
for i in Name1:
    print(i)

# Using List comprehension
List = (char for char in Name3)
for i in List:
    print(i)

# Length of the string
print(len(Name2))

# To check for a char or substring in a string
# Gives the index number
print(Name2.find("v"))

# Slicing in string
print(Name1[2:8])

# Slicing from the start
print(Name1[:8])

# Slicing from the end
print(Name1[5:])

# Negative Indexing
print(Name1[-7:-1])
print(Name1[-7:])

# For converting characters to uppercase
Str1 = "New York"
Str2 = Str1.upper()
print(Str2)

# For converting characters to lowercase
Str3 = Str1.lower()
print(Str3)

# For capitalising the first letter of a string
Str4 = Str1.capitalize()
print(Str4)

# For Stripping/removing any trailing whitespaces
str5 = Name4.strip()
print(str5)

# Replace a Substring
Replacing = Name2.replace("Ravi","Vanshika",1)
print(Replacing)

# Split a String into A listof substring
Spliting = Name2.split(" ",1)
print(Spliting)

# Concatenation
print(Name1 + Name2)
print(Name1 , Name2)

# String Formating
Formating = "My Name is {F1} and my father name is {F2}".format(F1 = Name1,F2 = Name2)
print(Formating)

# Escape Characters
# \' -> Single Quote   '
# \\ -> Backslash      \
# \n -> New Line     
# \r -> Carriage Return
# \t -> Tab   
# \b -> Backspace
# \f -> Form Feed
# \ooo -> Octal value
# \xhh -> Hex value
print("My Dad\'s son\\daughter \n They are\tgreat")