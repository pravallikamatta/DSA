str = "banana"
freq={}
for i in str:
   if i in freq:
      freq[i]+=1
   else:
       freq[i]=1
print(max(freq, key=freq.get)) 
#freq.get('b') → 1
#freq.get('a') → 3
#freq.get('n') → 2      