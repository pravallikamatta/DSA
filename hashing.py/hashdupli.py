arr = [10,12,14,12,15]

freq={}

for i in arr:
    if i in freq:
         freq[i]+=1
    else:
         freq[i]=1
for key, value in freq.items():
   if value>1:
      print("true")              
