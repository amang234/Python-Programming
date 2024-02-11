# Arithmetic Operators
num1 = int(input("Enter the Number 1: "))
num2 = int(input("Enter the Number 2: "))
num3 = int(input("Enter the Number 3: "))
num4 = int(input("Enter the Number 4: "))

# Addition
sum = num1+num2
# Subtraction
diff = num1 - num2
# Multipliication
Multi = num1 * num2
# Division
Divi = num1 / num2
# Moodulus
Modu = num1 % num2
# Exponential
expo = num1 ** num2
# Floor Division
FD = num1//num2
print("Addition ",sum)
print("Subtraction ",diff)
print("Multiplication ",Multi)
print("Division ",Divi)
print("Modulus ",Modu)
print("Exponential ",expo)
print("Floor Division ",FD)


# Assignment Operator
num3 = num1
print(num1,num2,num3)
num3 += num1
print(num1,num2,num3)
num3 -= num1
print(num1,num2,num3)
num3 *= num1
print(num1,num2,num3)
num3 /= num1
print(num1,num2,num3)
num3 %= num1
print(num1,num2,num3)
num3 //= num1
print(num1,num2,num3)
num3 **= num1
print(num1,num2,num3)
num3 &= num1
print(num1,num2,num3)
num3 |= num1
print(num1,num2,num3)
num3 ^= num1
print(num1,num2,num3)
num3 >>= num1
print(num1,num2,num3)
num3 <<= num1
print(num1,num2,num3)

#Comparison Operators
print(num1==num2)
print(num1!=num2)
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)

#Logical Operators
exp1 = num1 > num2
exp2 = num3 < num4
print("Exp1 and Exp2: " , exp1 and exp2)
print("Exp1 or Exp2: " , exp1 or exp2)
print("Not Exp2: " , not exp2)

# Identity Operators
print("If num1 is num2" , num1 is num2)
print("If num1 is not num2" , num1 is not num2)

# Membership Operators
Fruits = ("Apple","banana","cherry")
print("Is banana present in fruits" , "banana" in Fruits)
print("Is mango present in fruits" , "mango" not in Fruits)

# Bitwise Operators
print("AND",num1 & num2)
print("Or",num1 | num2)
print("Xor",num1 ^ num2)
print("Not",~num2)
print("Left Shift",num1 << num2)
print("Right Shift",num1 >> num2)

# Operators Precedense
x = 2
y = 3
z = 4
a = 5
b = 8
op = y + x ** z / x * a - b // x
print(op)