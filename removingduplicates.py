x=int(input("Enter the number:"))
l=[]
for i in range(x):
    y=int(input("Enter the number:"))
    l.append(y)

temp=set(l)
print(list(temp))

#optimal solution
'''
x = int(input("Enter the number of elements: "))
l = set(int(input("Enter a number: ")) for _ in range(x))
print(list(l))
'''