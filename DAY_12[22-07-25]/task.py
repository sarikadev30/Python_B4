# Multi Dimensional List => nested list

# mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# print(mat[0][1])
# print(mat[2][3])

# for i in range(len(mat)):
#     for j in range(len(mat[0])):
#         print(mat[i][j], end=" ")
# 1 2 3 4 5 6 7 8 9 10 11 12
# 0 => j=> 0 1 2 3
# 1 => j=> 0 1 2 3
# 2 => j=> 0 1 2 3

mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

# 1 5 9 2 6 10 3 7 11 4 8 12
# ................................................................
# Calculate sum

# .................................................................
mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

#  1 2 3 4 8 7 6 5 9 10 11 12 16 15 14 13

# ........................................................................
# 1 5 9 13 14 10 6 2 3 7 11 15 16 12 8 4

# ...................................................................

"""

### **Sum of Border Elements**

For the 2D list below:

```python
items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

```

Write a program to calculate the sum of the border elements 
(elements on the outer edge of the 2D list).
items = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Expected Output:
`Sum of border elements: 40`
"""
