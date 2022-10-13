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
w = np.array([-1, -1, -1])

xs = [u[0], v[0], w[0]]
ys = [u[1], v[1], w[1]]
zs = [u[2], v[2], w[2]]

ax.scatter(xs, ys, zs)
plt.show()
