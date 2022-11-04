import numpy as np

d1 = np.array([2, 3, 4]).reshape((3, 1))

A = np.array([[1, 1, 1, 1],
              [1, 2, 2, 2],
              [1, 2, 3, 4]])

print('d1=\n', d1)
print('A=\n', A)

print('d1.shape=\n', d1.shape)  # (3, 1)
print('A.shape=\n', A.shape)    # (3, 4)

print('d1 * A=\n', d1 * A)
# [[ 2  2  2  2]
#  [ 3  6  6  6]
#  [ 4  8 12 16]]

# A[i, :] *= d[i]
