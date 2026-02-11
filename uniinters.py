A = [2, 3, 4, 7, 8]
B = [2, 3, 4, 9, 10]
temp = (A + B)
inter = []
union = []
for i in temp:
    if i not in union:
        union.append(i)
for j in B:
    if j in A:
        inter.append(j)        
 
print(inter)
print(union)
