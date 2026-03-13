s = "loveleetcode"
hash = {}
for i in s:
    if i in hash:
        hash[i]+=1
    else:
        hash[i]=1

for i in range(len(s)):
    if hash[s[i]] == 1:
        print(i)
        break
else:
    print(-1)            