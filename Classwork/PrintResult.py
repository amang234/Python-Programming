# print(2**3**4)

# num = 6+4**6//6
# print(num)

# A = 0b10111101  
# B = 0b0000010   
# result = A ^ B
# print(bin(result))

# Rows = int(input("Enter the Number of Rows: "))

# for i in range(Rows, 0, -1):
#     for j in range(Rows-i):
#         print(" ", end="")
#     for j in range(i):
#         print("* ", end="")
#     print()

# for i in range(Rows, 0, -1):
#     for j in range(Rows-i):
#         print(" ", end="")
#     for j in range(i):
#         print("| ", end="")
#     print()


# for i in range(1, Rows + 1):
#     if i <= Rows:
#         print("| " * i)
#     else:
#         print("| " * (Rows - i + 1))

# for i in range(Rows-1, 0, -1):
#     if i < Rows:
#         print("| " * i)
#     else:
#         print("| " * (Rows - i + 1))


n= 3
for i in range(n):
   for j in range(i+1):
        if(i%2!=0):
           print("*",end=" ")
        else:
           print(i,end=" ")       
   print()
        