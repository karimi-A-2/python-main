import numpy as np

A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b = A[:, 1]
b
A
b[1] = 10000
b
A

b = A[:, 0].copy()
b
b[1] = -20000
b
A
