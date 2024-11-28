def rev(text):
    for i in range(len(text)-1,-1,-1):
        print(text[i],end="")
text=input("Enter the string:")
result=rev(text)
print(result)