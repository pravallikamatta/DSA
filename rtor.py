arr = [1, 2, 3, 4]
n = len(arr)
for i in range(n-2,-1,-1):
   arr[i+1]=arr[i]  
arr[0] = n
print(arr)   