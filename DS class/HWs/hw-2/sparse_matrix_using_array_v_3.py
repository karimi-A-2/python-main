
# if we know elements are only 0 and 1 then
from typing import List

sparse_mat = [[1, 0, 1, 0, 1],
              [0, 1, 1, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0]]

rowNum_colNum_value: List[List[int]] = [[], []]

rows = len(sparse_mat)
cols = len(sparse_mat[0])

k = 0
for i in range(rows):
    for j in range(cols):
        if sparse_mat[i][j] != 0:
            rowNum_colNum_value[0].append(i)
            rowNum_colNum_value[1].append(j)
            k += 1

print(rows, "*", cols, "matrix")
print("no 1:", k)
print("row num:", rowNum_colNum_value[0])
print("col num:", rowNum_colNum_value[1])
