n= int(input("Enter The Number: "))


# Print N to 1
def Nto1(n):
    if n<1:
        return
    print(n)
    Nto1(n-1)

Nto1(n)

# Print 1 to N
def Start1toN(n):
    if n<1:
        return
    Start1toN(n-1)
    print(n)

Start1toN(n)