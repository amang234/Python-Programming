# While Loops
i = 0
while i<=10:
    print(i)
    i+=1

# Predict The Output
# Q1
x = 1
while x==1:
    x-=1
    print(x)

# Q2
i = 10
while i==20:
    print("computer buff!!")

# Q3
x=4
y=0
while x>=0:
    x-=1
    y+=1
    if x==y:
        continue
    else:
        print(x,y)

# Q4
x=4
y=0
while x>=0:
    if x==y:
        break
    else:
        print(x,y)
    x-=1
    y+=1    