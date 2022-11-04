import numpy as np
import timeit

m, n, p = 100, 50, 2000

A = np.random.rand(m, n, p)
s = np.random.rand(p)

B = np.array(A)


def f1():
    for i in range(p):
        A[:, :, i] *= s[i]


def f2():
    global B
    B *= s


t_1 = timeit.timeit(f1, number=100) / 100
print(t_1)  # 0.03370673041

s = s.reshape((1, 1, 2000))
t_2 = timeit.timeit(f2, number=100) / 100
print(t_2)  # 0.004424425410000001  # 7 times faster

