arr=[2,4,1,3,5,7]
even=0
odd=0
for i in range(len(arr)):
    if arr[i]%2==0:
        even+=1
    else:
        odd+=1    
print("odd are",odd)
print("even are",even)       
