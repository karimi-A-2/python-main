import numpy as np

A = np.zeros((4, 6))
A
A = np.zeros((4, 6), dtype=np.int32)
A
A = np.ones((3, 7))
A
A = np.ones((3, 8), dtype=np.uint8)
A
np.full((4, 3), 50.0)
A = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
A
A[1, 2]
A[0, -1]
A.shape
A.shape[0]
A.shape[1]
A.shape[::-1]
A.size  # 12
A.ndim  # 2
A[0, :]  # array([1, 2, 3, 4])
A[0, :].shape  # (4,)
A[[0], :]  # array([[1, 2, 3, 4]])
A[[0], :].shape  # (1, 4)
A[:, 2]
A[:, [2]]
A[:, 2].shape
A[:, [2]].shape
A[1:3]
A[1:3, :]
A[:, :3]
A[:, ::2]
A[:, ::-1]
r = np.array([0, 1, 0, 2, 2])
A
r
A[r, :]
A
A[:, 0] = 1
A
A[:, 0] = [20, 30, 40]
A
A.T
B = np.array([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3]])
A
B
A + B
A * B

np.dot(A, B)  # A @ B
A.dot(B)  # A @ B
A @ B  # A @ B

A.dot(B.T)

I = np.eye(3)
I
np.random.random((2, 3))
np.random.random((2, 3))
np.random.random((2, 3))
np.random.rand(2, 3)
np.random.rand(2, 3)
np.random.randn(2, 3)
np.random.randn(2, 3)
