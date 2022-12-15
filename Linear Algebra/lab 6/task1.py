import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('macosx')

from face_data import Face1, Face2, Face3, TargetFace2, edges


def plot_face(plt, X, edges, color='b'):
    "plots a face"
    
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


TargetFace = TargetFace2
NoisyTargetFace = TargetFace + 3 * np.random.randn(*TargetFace.shape)

face1 = Face1.ravel()
face2 = Face2.ravel()
face3 = Face3.ravel()
t = NoisyTargetFace.ravel()

F = np.stack((face1, face2, face3), axis=1)
t = t.reshape((136, 1))

for i in range(5):
    inds = np.random.choice(range(136), 3, replace=False)
    faces = F[inds, :]
    target = t[inds, :]
    x1 = np.linalg.solve(faces, target)
    a1, b1, c1 = x1.ravel().tolist()
    
    sum_squares_1 = sum(((F @ x1) - t) ** 2)
    print(i, ">rnd sum square=", sum_squares_1)
    
    # x2 = np.linalg.inv(F.T @ F) @ F.T @ t
    x2, *_ = np.linalg.lstsq(F, t, rcond=None)
    a2, b2, c2 = x2.ravel().tolist()
    
    sum_squares_2 = sum(((F @ x2) - t) ** 2)
    print(i, ">lsq sum square=", sum_squares_2)
    
    Face_rnd = a1 * Face1 + b1 * Face2 + c1 * Face3
    Face_lsq = a2 * Face1 + b2 * Face2 + c2 * Face3
    
    plot_face(plt, TargetFace, edges, color='r')  # original => red
    plot_face(plt, NoisyTargetFace, edges, color='k')  # noisy => black
    plot_face(plt, Face_rnd, edges, color='g')  # rnd => green
    plot_face(plt, Face_lsq, edges, color='b')  # lsq => blue
    
    plt.show()
