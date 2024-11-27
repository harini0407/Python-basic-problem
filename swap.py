num1=int(input("Enter the number 1"))
num2=int(input("Enter the number 2"))


def swap(a,b):
    a,b=b,a
    return a,b

print("Value of num1 before swapping",num1)
print("Value of num2 before swapping",num2)
res_num=swap(num1,num2)
print("Value of num1 and num2 after swapping",res_num)



