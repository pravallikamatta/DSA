str = (input("enter str:")).lower().replace(" ", "")
freq={}

for i in str:
    if i in sorted(freq):
        freq[i]+=1
    else:
        freq[i]=1
        
print(freq)         
           ##or##
print("method2")
freq.get(i, 0) + 1
print(freq)

