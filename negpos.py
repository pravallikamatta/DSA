arr = [2, -2, 3, -6, 1, 8]
neg = []
pos = []

for i in arr:
    if i>0:
        pos.append(i)
    else:
        neg.append(i)

print(pos + neg)        


