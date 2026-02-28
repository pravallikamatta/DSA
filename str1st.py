str = "pravalli"
freq={}
for i in str:
   freq[i] = freq.get(i, 0) + 1
for i in str:
   if  freq[i]==1:
        print(i)
        break
   #here using 'break' is very imp for loop will conti
   #and prints all single repeated

