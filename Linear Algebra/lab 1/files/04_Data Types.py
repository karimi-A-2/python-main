import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.int64)   # 8 bytes
b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.int32)   # 4 bytes
c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.int16)   # 2 bytes
d = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.int8)    # 1 bytes
e = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.uint8)   # 1 bytes
print(a.nbytes, b.nbytes, c.nbytes, d.nbytes, e.nbytes)
d - 4  # array([-3, -2, -1,  0,  1,  2,  3,  4,  5,  6], dtype=int8)
e - 4  # array([253, 254, 255,   0,   1,   2,   3,   4,   5,   6], dtype=uint8)
f = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float32)     # 4 bytes
g = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float64)     # 8 bytes
# h = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.float128)    # 16 bytes  # not supported

print(f.nbytes, g.nbytes)  # 40 80
l = np.array([False, True, True])
l.dtype
l = np.array([0, 1, 1], dtype=np.bool_)
l.dtype
l.nbytes  # 3
