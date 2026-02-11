arr = [2,1,21,5,10]
high = arr[0]
low = arr[0]
for i in range(1,len(arr)):
    if arr[i]>high:
        high=arr[i]
    elif arr[i]<low:
        low=arr[i]
    else:
        print("error")        
print(high)    
print(low)
