def prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n%i==0:#n=10 i=2 10%2==0 10%3==0 10%4==0 10%5==0
            return False
    return True

n=int(input())
for i in range(n):
    if prime(i):
        print(i)
