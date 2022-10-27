import numpy as np
import timeit

n = 1000

A = np.random.rand(100, 200)
d1 = np.random.rand(100)
D1 = np.diag(d1)
d1 = d1.reshape(100, 1)


def f_star():
    d1 * A


def f_at():
    D1 @ A


t_star = timeit.timeit(f_star, number=1000) / 1000
t_at = timeit.timeit(f_at, number=1000) / 1000

print(t_star)       # 8.058375000000006e-06
print(t_at)         # 8.372479199999999e-05
