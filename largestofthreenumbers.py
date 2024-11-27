
num1=int(input())
num2=int(input())
num3=int(input())
def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
    
result=largest(num1,num2,num3)
print("Largest number is",result)
