x=int(input("Enter the number:"))
l=[]
for i in range(x):
    y=int(input("Enter the number:"))
    l.append(y)

temp=set(l)
print(list(temp))