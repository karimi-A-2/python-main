import numpy as np

m, n, p = 100, 50, 2000

A = np.random.rand(m, n, p)
s = np.random.rand(p)

B = np.array(A)

for i in range(p):
    A[:, :, i] *= s[i]

# s = s.reshape((1, 1, 2000))
B *= s

print(A == B)
