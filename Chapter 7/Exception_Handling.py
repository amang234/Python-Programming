a = int(input("Enter a: "))
b = int(input("Enter b: "))

try:
    result = a/b
except ZeroDivisionError:
    result = None   
    print("Error: Cannot be divided by 0")
finally:
    print("Division Operation Completed", result)