# Check if a substring is present in a string
string = input("Enter The String: ")
substring = input("Enter the substring")
if substring in string :
    print(substring, "is present in", string)
else:
    print(substring, "is not present in", string)