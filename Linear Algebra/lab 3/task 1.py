import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('macosx')

# create a (3 x 2) matrix
A = np.array([[1, 2],
              [3, 4],
              [-2, 1]])

fig = plt.figure()

# A 1 by 2 subplot grid, subplot 1 (3D)
ax1 = fig.add_subplot(1, 2, 1, projection='3d')
ax1.set_title('column space')

u = np.random.randn(2, 200)  # (2 x 200)
v = A @ u  # (3 x 2) (2 x 200) = (3 x 200)
ax1.scatter(v[0, :], v[1, :], v[2, :], color='b')

tail = np.zeros((3, 2), int)
ax1.quiver(tail[0, :], tail[1, :], tail[2, :], A[0, :], A[1, :], A[2, :], color='r')


# A 1 by 2 subplot grid, subplot 2 (2D)
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title('row space')

u = np.random.randn(200, 3)  # (200 x 3)
v = u @ A  # (200 x 3) (3 x 2) = (200 x 2)
ax2.plot(v[:, 0], v[:, 1], 'ro')
ax2.plot(A[:, 0], A[:, 1], 'go')

plt.show()
