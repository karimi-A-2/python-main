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

a, b = np.random.rand(2)
w = a * u + b * v
ax.scatter(w[0], w[1], w[2], color='b')

plt.show()
