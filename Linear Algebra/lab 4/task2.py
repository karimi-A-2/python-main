import numpy as np

m, n, p = 100, 50, 2000

A = np.random.rand(m, n, p)     # (100, 50, 2000)
s = np.random.rand(p)           # (2000,)

B = np.array(A)

for i in range(p):  # 2000
    A[:, :, i] *= s[i]  # A[:, :, 0] *= s[0]

s = s.reshape((1, 1, 2000))     # (1, 1, 2000)
B *= s

print(A == B)
