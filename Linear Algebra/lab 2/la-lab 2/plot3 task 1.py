import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
matplotlib.use('macosx')

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# plot multiple points
u = np.array([1, 2, 3])
v = np.array([2, 0, -2])

xs = [u[0], v[0]]
ys = [u[1], v[1]]
zs = [u[2], v[2]]

# base of the vectors set to the origin
tail_x = [0, 0]
tail_y = [0, 0]
tail_z = [0, 0]

ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)

ax.quiver(tail_x, tail_y, tail_z, xs, ys, zs, color='r')

for _ in range(200):
    a, b = np.random.rand(2)
    w = a * u + b * v
    ax.scatter(w[0], w[1], w[2], color='b')

plt.show()


'''
rand(d0, d1, ..., dn)

Random values in a given shape.
Note
This is a convenience function for users porting code from Matlab, and wraps random_sample.
That function takes a tuple to specify the size of the output, which is consistent with other NumPy functions like numpy.zeros and numpy.ones.
Create an array of the given shape and populate it with random samples from a uniform distribution over [0, 1).
d0, d1, ..., dn : int, optional
The dimensions of the returned array, must be non-negative. If no argument is given a single Python float is returned.
out : ndarray, shape (d0, d1, ..., dn)
Random values.
random
>>> np.random.rand(3,2)
array([[ 0.14022471,  0.96360618],  #random
       [ 0.37601032,  0.25528411],  #random
       [ 0.49313049,  0.94909878]]) #random
Returns:
Random values.
'''