t = (5, 2, 6, 3, 4, 1)
res = sorted(t, key=lambda x: (x != 2, x))  # custom sorting key
print(res)  # print the sorted result