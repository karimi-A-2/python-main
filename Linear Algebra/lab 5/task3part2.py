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


TargetFace2 += 3 * np.random.randn(*TargetFace2.shape)

face1 = Face1.ravel()
face2 = Face2.ravel()
face3 = Face3.ravel()
t = TargetFace2.ravel()

F = np.stack((face1, face2, face3), axis=1)

av_a, av_b, av_c = 0, 0, 0
N = 20
for i in range(N):
    inds = np.random.choice(range(136), 3, replace=False)
    faces = F[inds, :]
    target = t[inds].reshape((3, 1))
    x = np.linalg.solve(faces, target)
    # x = np.linalg.inv(faces) @ target
    a, b, c = x.ravel().round(decimals=3).tolist()
    
    av_a += a
    av_b += b
    av_c += c

av_a /= N
av_b /= N
av_c /= N

Face = av_a * Face1 + av_b * Face2 + av_c * Face3
plot_face(plt, TargetFace2, edges, color='r')
plot_face(plt, Face, edges, color='g')
plt.show()
