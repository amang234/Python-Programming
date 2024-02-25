# Pass By value
def addOne(x):
    x= x+1
    print("Inside Function",x)

x =5
addOne(x)
print("Outside Function",x)


# Pass By Reference
def modifyList(lst):
    # lst.append(4)
    lst = [4,5,6]
    print("Inside Function",lst)

lst = [1,2,3]
modifyList(lst)
print("Outside Function",lst)
