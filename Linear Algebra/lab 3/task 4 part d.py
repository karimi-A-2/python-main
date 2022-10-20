import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from face_data import Face1, edges

matplotlib.use('macosx')


def plot_face(plt, X, edges, color='b'):
    """plots a face"""
    plt.plot(X[:, 0], X[:, 1], 'o', color=color)
    
    for i, j in edges:
        xi, yi = X[i]
        xj, yj = X[j]
        
        plt.plot((xi, xj), (yi, yj), '-', color=color)
        
        plt.axis('square')
        plt.xlim(-100, 100)
        plt.ylim(-100, 100)


rng = np.linspace(-0.7, 0.7, 100)

for s in rng:
    plt.cla()
    
    A = np.array([
        [1, 0],
        [s, 1]
    ])
    X = Face1 @ A
    
    plot_face(plt, X, edges, color='b')
    
    plt.draw()
    plt.pause(.01)

plt.show()
