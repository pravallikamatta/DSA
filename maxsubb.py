arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
maxx = arr[0]
curr = arr[0]

for i in range(1, len(arr)):
    curr = max(arr[i], curr + arr[i])
    maxx = max(maxx, curr)



print("Largest sum:", maxx)