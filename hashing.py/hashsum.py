nums = [3, 8, 12, 4, 6]
target=10
hash={}
for i in range(len(nums)):
    x = target-nums[i]
    if x in hash:   
        print(hash[x],i)
        break
    hash[nums[i]] = i