arr = [1, 2, 2, 3, 1, 4, 2]

freq = {}   # empty dictionary (hash map)

for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for key, value in freq.items():
   print(key,"=", value)         