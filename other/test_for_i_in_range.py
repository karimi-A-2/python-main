
size = 10
rows, cols = 3, size

print([0 for i in range(cols)])

compactMatrix = []
for j in range(rows):
    temp = [0 for i in range(cols)]
    compactMatrix.append(temp)

print(compactMatrix)
