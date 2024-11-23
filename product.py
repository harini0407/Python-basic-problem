'''Creating a program that takes 2 numbers as input and prints their project'''
num1=int(input("Enter the number 1"))
num2=int(input("Enter the number 2"))
def prod(x,y):
    product_x=x*y
    return product_x

result=prod(num1,num2)
print("The product of numbers is",result)
            