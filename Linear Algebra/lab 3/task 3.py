import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

matplotlib.use('macosx')

# create a (3 x 2) matrix
A = np.array([[1, 2, 1],
              [2, -1, -1],
              [-1, 1, -2]])
B = np.array([[1, 2, -3],
              [3, 1, 1],
              [2, 1, 0]])
C = np.array([[1, 2, -3],
              [3, 6, -9],
              [-2, -4, 6]])

matrices = [A, B, C]
matrices_names = ["A", "B", "C"]

fig = plt.figure()

for i in range(3):
    M = matrices[i]
    M_name = matrices_names[i]
    
    # A 2 by 3 subplot grid, subplot (1 + i) (3D)
    ax = fig.add_subplot(2, 3, (1 + i), projection='3d')
    ax.set_title(f'row space {M_name}')
    
    u = np.random.randn(200, 3)  # (200 x 3)
    v = u @ M  # (200 x 3) (3 x 3) = (200 x 3)
    ax.scatter(v[:, 0], v[:, 1], v[:, 2], color='r')
    
    tail = np.zeros((3, 3), int)
    ax.quiver(tail[:, 0], tail[:, 1], tail[:, 2], M[:, 0], M[:, 1], M[:, 2], color='b')
    
    # A 2 by 3 subplot grid, subplot (4 + i) (3D)
    ax = fig.add_subplot(2, 3, (4 + i), projection='3d')
    ax.set_title(f'column space {M_name}')
    
    u = np.random.randn(3, 200)  # (3 x 200)
    v = M @ u  # (3 x 3) (3 x 200) = (3 x 200)
    ax.scatter(v[0, :], v[1, :], v[2, :], color='b')
    
    tail = np.zeros((3, 3), int)
    ax.quiver(tail[0, :], tail[1, :], tail[2, :], M[0, :], M[1, :], M[2, :], color='r')

plt.show()
