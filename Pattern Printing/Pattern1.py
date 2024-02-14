# Pattern 1
# for n=1 print *****
# for n=2 print *****
#               *****
n = int(input("Enter the Number of rows: "))
for _ in range(n):
    print("*" * 5)
    
# Pattern 2
# for n=4 print 1234    for n=6 print 123456
#               1234                  123456
#               1234                  123456
#               1234                  123456
#                                     123456
#                                     123456
n = int(input("Enter the Number of rows: "))
for i in range(n):
    for j in range(1,n+1):
        print(j,end="")
    print()

# Pattern 3
# for n=4 print 1
#               12
#               123
#               1234
n = int(input("Enter the Number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()

# Pattern 4
# for n=4 print A
#               AB
#               ABC
#               ABCD
n = int(input("Enter the Number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end="")
    print()

# Pattern 5
n=int(input("Enter The number: "))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    for j in range(1,2*i):
        print(j,end="")
    print()