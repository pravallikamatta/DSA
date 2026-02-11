arr = [1, 2, 9, 5]
flag = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        flag = False
        break

if flag:
    print("Array is sorted")
else:
    print("Array is not sorted")
