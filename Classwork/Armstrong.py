def is_armstrong_number(number):
    num_digits = len(str(number))
    
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** num_digits
        temp //= 10
    
    # Check if the number is equal to the sum
    return number == sum

# Test the function
number = 153
print(f"{number} is Armstrong: {is_armstrong_number(number)}")

number = 370
print(f"{number} is Armstrong: {is_armstrong_number(number)}")

number = 371
print(f"{number} is Armstrong: {is_armstrong_number(number)}")

number = 9474
print(f"{number} is Armstrong: {is_armstrong_number(number)}")

number = 9475
print(f"{number} is Armstrong: {is_armstrong_number(number)}")
