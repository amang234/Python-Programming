# # list = [1,2,3,4,5]
# string ([0:3])
# string ([:1])
# string ([0:3])
# string ([::-1])
# string ([0:3P])

# # Grade System
# Marks = int(input("Enter your Marks: "))

# if Marks <= 40:
#     print("F Grade")
# elif Marks <= 50:
#     print("E Grade")
# elif Marks <= 60:
#     print("D Grade")
# elif Marks <= 70:
#     print("C Grade")
# elif Marks <= 80:
#     print("B Grade")
# elif Marks <= 90:
#     print("A Grade")
# elif Marks <= 100:
#     print("S Grade")
# else:
#     print("No extra Marks")

# Nested
n = int(input("Enter the Number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()