matrix = [
    [1, 3, 5],
    [7, 9, 11],
    [13, 15, 17]
]

target = 9

rows = len(matrix)
cols = len(matrix[0])

i = 0          
j = cols - 1    

found = False

while i < rows and j >= 0:
    
    if matrix[i][j] == target:
        print("Found at", i, j)
        found = True
        break

    elif matrix[i][j] > target:
        j -= 1      

    else:
        i += 1 
if not found:
    print("Not found")
