import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('macosx')

from face_data import Face1, Face2, Face3, TargetFace2, edges


def plot_face(plt, X, edges, color='b'):
    """plots a face"""
    
    plt.plot(X[:, 0], X[:, 1], 'o', color=color, markersize=3)
    
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


face1 = Face1.ravel()
face2 = Face2.ravel()
face3 = Face3.ravel()
t = TargetFace2.ravel()

F = np.stack((face1, face2, face3), axis=1)

faces = F[0:3, :]
target = t[0:3].reshape((3, 1))
x = np.linalg.solve(faces, target)  # (3, 1)
# x = np.linalg.inv(faces) @ target
a, b, c = x.ravel().round(decimals=3).tolist()
print(a, b, c)
Face = a * Face1 + b * Face2 + c * Face3

plot_face(plt, TargetFace2, edges, color='r')
plot_face(plt, Face, edges, color='g')

plt.show()
