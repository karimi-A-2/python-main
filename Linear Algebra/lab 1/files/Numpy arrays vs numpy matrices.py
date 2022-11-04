import numpy as np

A = np.array([[1, 2, 3], [1, 1, 1], [-1, -2, -1]])
A
A * A  # element-wise multiplication
A.dot(A)  # matrix multiplication
A @ A  # matrix multiplication (same as above)

M = np.matrix([[1, 2, 3], [1, 1, 1], [-1, -2, -1]])
M
M * M  # M @ M
np.multiply(M, M)  # M * M

M = np.mat(A)  # array to Matrix
M
M = np.matrix(A)  # array to Matrix
M
M.T  # Transpose
M.I  # Inverse
M.I * M
M * M.I
M.A  # matrix to array
type(M)
type(M.A)

C = np.matrix("1 2; 3 4; 5 6")
C
M * C
