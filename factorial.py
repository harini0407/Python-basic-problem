num=int(input())
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)



result=fact(num)
print("factorial is:",result)

