nums = [2, 2, 1, 1, 2, 2, 2]
length = len(nums)
hash={}
for i in nums:
    if i in hash:
        hash[i]+=1
    else:    
     hash[i]=1

for key, value in hash.items():
    if value > length // 2:
        print(key)        