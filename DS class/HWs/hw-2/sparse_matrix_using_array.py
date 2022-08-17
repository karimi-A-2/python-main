# Python program for Sparse Matrix Representation
# using arrays

# assume a sparse matrix of order 4*5
# let assume another matrix compactMatrix
# now store the value,row,column of arr1 in sparse matrix compactMatrix

sparse_mat = [[0, 0, 3, 0, 4],
              [0, 0, 5, 7, 0],
              [0, 0, 0, 0, 0],
              [0, 2, 6, 0, 0]]

# initialize size as 0
size = 0

for i in range(4):
    for j in range(5):
        if sparse_mat[i][j] != 0:
            size += 1

# number of columns in compactMatrix(size) should
# be equal to number of non-zero elements in sparseMatrix
rows, cols = (3, size)
rowNum_colNum_value = []
for j in range(rows):
    zeros = [0 for i in range(cols)]
    rowNum_colNum_value.append(zeros)

k = 0
for i in range(4):
    for j in range(5):
        if sparse_mat[i][j] != 0:
            rowNum_colNum_value[0][k] = i
            rowNum_colNum_value[1][k] = j
            rowNum_colNum_value[2][k] = sparse_mat[i][j]
            k += 1

for i in rowNum_colNum_value:
    print(i)
