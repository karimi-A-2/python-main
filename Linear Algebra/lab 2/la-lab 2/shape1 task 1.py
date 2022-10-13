import matplotlib
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('macosx')

n = 11
x1 = np.cos(np.linspace(0, np.pi, n))
y1 = np.sin(np.linspace(0, np.pi, n))
S1 = np.vstack((-x1, y1 - .7))  # (2, 11)
S1 = S1.T  # (11, 2)

x2 = np.linspace(-1.2, 1.2, n)
y2 = np.zeros(n)
S2 = np.vstack((x2, y2))  # (2, 11)
S2 = S2.T  # (11, 2)

S3 = 0.5 * S1 + 0.5 * S2

plt.plot(S1[:, 0], S1[:, 1], 'bo-')
plt.plot(S2[:, 0], S2[:, 1], 'ro-')
plt.plot(S3[:, 0], S3[:, 1], 'go-')

plt.axis('equal')
plt.xlim(-2, 2)
plt.ylim(-2, 2)

plt.show()
