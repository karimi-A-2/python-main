import numpy as np

A = np.zeros((2, 4, 3))
A
A.shape
A[:, :, 0].shape
A[:, :, 0] = [[1, 2, 3, 4], [5, 6, 7, 8]]
A[:, :, 1] = [[2, 2, 2, 2], [4, 4, 4, 4]]
A[:, :, 2] = [[10, 20, 30, 40], [11, 21, 31, 41]]
A
A[0, :, :]
A[0]
A[:, 1, :]
A[:, 1]
A[:, [1]]
A[:, 1].shape
A[:, [1]].shape
A[:, :, 0]
A[:, :, 2]
A[:, 2:, 2]
A.ravel()
