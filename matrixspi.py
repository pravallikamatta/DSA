matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
top = 0 #0
bottom = len(matrix)-1 #2
left=0 #0
right =len(matrix[0])-1 #2
 
while top <= bottom and left <= right:

    # left → right
    for i in range(left, right + 1):
        print(matrix[top][i], end=" ")
    top += 1

    # top → bottom
    for i in range(top, bottom + 1):
        print(matrix[i][right], end=" ")
    right -= 1

    if top <= bottom:
        # right → left
        for i in range(right, left - 1, -1):
            print(matrix[bottom][i], end=" ")
        bottom -= 1

    if left <= right:
        # bottom → top
        for i in range(bottom, top - 1, -1):
            print(matrix[i][left], end=" ")
        left += 1
