import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('macosx')

from face_data import Face1, Face2, Face3, edges


def plot_face(plt, X, edges, color='b'):
    """plots a face"""
    
    plt.plot(X[:, 0], X[:, 1], 'o', color=color)
    
    # i, j = edges[0]  # edge from node i to node j
    for i, j in edges:
        xi = X[i, 0]
        yi = X[i, 1]
    
        xj = X[j, 0]
        yj = X[j, 1]
        # draw a line between X[i] and X[j]
        plt.plot((xi, xj), (yi, yj), '-', color=color)
    
    plt.axis('square')
    plt.xlim(-100, 100)
    plt.ylim(-100, 100)


# rng = np.linspace(0, 1, 20)  # inclusive
rng = np.linspace(-0.5, 1.5, 20)  # inclusive
faces = [Face1, Face2, Face3]
for i in range(12):
    for alpha in rng:
        plt.cla()
        face = (1 - alpha) * faces[i % len(faces)] + alpha * faces[(i + 1) % len(faces)]
        plot_face(plt, face, edges, color='b')
        plt.draw()
        plt.pause(.001)
plt.show()
