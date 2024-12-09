t = (5, 2, 6, 3, 4, 1)
res = sorted(t, key=lambda x: (x != t[1], x))  
print(res) 