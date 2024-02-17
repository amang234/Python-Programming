# Given a list in Python and provided the index of the elements,
# Write a program to swap the two elements in the list.
# Examples:
# Input : List = [23, 65, 19, 90], idxl = O, idx2 = 2
# Output : [19, 65, 23, 90]
# Input : List = [l, 2, 3, 4, 5], idxl =1, idx2 = 4
# Output : [1, 5, 3, 4, 2]

n= int(input("Enter the size of list: "))
List =[]
for i in range(n):
    num=int(input())
    List.append(num)

print(List)
idx1= int(input("Enter the First index: "))
idx2= int(input("Enter the Second index: "))
temp=List[idx1]
List[idx1]=List[idx2]
List[idx2]=temp
print(List)