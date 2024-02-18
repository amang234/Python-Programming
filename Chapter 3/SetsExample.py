# Given three arrays, we have to find common elements in three
# sorted lists using sets.
# Input : arl = [l, 5, 10, 20, 40, 80]
#         ar2 = [6, 7, 20, 80, 100]
#         ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
# Output : [80, 20]

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

Set1 = set(ar1)
Set2 = set(ar2)
Set3 = set(ar3)
print("ar1 =",Set1)
print("ar2 =",Set2)
print("ar3 =",Set3)

Set1n2 = Set1.intersection(Set2)
FinalSet = Set1n2.intersection(Set3)
print("Common elements:",FinalSet)



# Input : arl = [l, 5, 5]
#         ar2 = [3, 4, 5, 5, 10]
#         ar3 = [5, 5, 10, 20]
# Output : [5]

arr1 = [1, 5, 5]
arr2 = [3, 4, 5, 5, 10]
arr3 = [5, 5, 10, 20]

set1 = set(arr1)
print("ar1 =",set1)
set2 = set(arr2)
print("ar1 =",set2)
set3 = set(arr3)
print("ar2 =",set3)

set1set2 = set1.intersection(set2)
set1set2set3 = set1set2.intersection(set3)
print("common elements:",set1set2set3)