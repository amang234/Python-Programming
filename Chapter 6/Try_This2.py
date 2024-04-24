# Write a Python function that checks 
# if the given string is at palindrome or not.
String = input("Enter a string: ")

def check_palindrome(String):
    clean_String = (String.replace(" ","")).lower()
    Reversed_String = clean_String[::-1]
    if clean_String == Reversed_String:
        print("It is a palindrome")
    else: 
        print("It is not a palindrome")
check_palindrome(String)