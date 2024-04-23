

n = 5


# for i in range(n):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(j,n):
#         print("*",end=" ")
#     print()


# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for j in range(i,5):
#         print("*  ",end=" ")
#     print()

rows = 3
k = 0
for i in range(rows, 0, -1):
    for j in range(rows - i):
        print("  ", end="")
    for j in range(2 * i - 1):
        print("* ", end="")
    print()


# for i in range(n):
#     for j in range(i):
#         print(" ",end=" ")
#     for k in range(i,5):
#         print("*  ",end=" ") 
#     print()



# for i in range(n):
#     for j in range (i+1):
#         print("*", end=" ")
#     print()
# for i in range(n):
#     for j in range (n-i-1):
#         print("*", end=" ")
#     print()
        
# for i in range(n):
#     for j in range (1,n+1):
#         print("*", end=" ")
#    print()