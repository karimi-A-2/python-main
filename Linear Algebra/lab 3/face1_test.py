import numpy as np

Face1 = np.array([
    [1, 0],
])

th = np.pi / 6

A = np.array([
    [np.cos(th), np.sin(th)],
    [-np.sin(th), np.cos(th)]
])

X = Face1 @ A
