def aver(l):
    sum=0
    for i in l:
        sum+=i
             
    return sum/len(l)

a=[1,2,3]
result=aver(a)
print("Average of the list is ",result)