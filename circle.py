radius=float(input("Enter the radius: "))

def area_C(r):
    circle=4*3.14*(r**2)
    return circle

result=area_C(radius)
print("Area of the circle is",result)
