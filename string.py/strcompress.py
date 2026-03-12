strg = input("enter the string:")
freq={}
for i in strg:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1    
res="".join(i + str(freq[i]) for i in freq)   
if len(strg)>=len(res):    
  print(res)
else:
    print(strg)     
