str ="pravallika".lower()
temp =[]

for i in str:
    if i not in temp:
     temp.append(i)
res="".join(temp)     

print(res)     
