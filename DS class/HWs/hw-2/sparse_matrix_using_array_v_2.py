sparse_mat = [[1, 0, 1, 0, 1],
              [0, 1, 1, 1, 0],
              [0, 1, 1, 0, 0],
              [0, 0, 0, 0, 0],
              [0, 1, 1, 0, 0]]

rowNum_colNum_value: list[list[int]] = [[], [], []]

rows = len(sparse_mat)
cols = len(sparse_mat[0])

k = 0
for i in range(rows):
    for j in range(cols):
        element = sparse_mat[i][j]
        if element != 0:
            rowNum_colNum_value[0].append(i)
            rowNum_colNum_value[1].append(j)
            rowNum_colNum_value[2].append(element)
            k += 1

print(rows, "*", cols, "matrix")
print("no non-zero elements:", k)
print("row num:", rowNum_colNum_value[0])
print("col num:", rowNum_colNum_value[1])
print("value  :", rowNum_colNum_value[2])
