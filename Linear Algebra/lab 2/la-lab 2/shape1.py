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

print(S1.shape)
print(S2.shape)

plt.plot(S1[:, 0], S1[:, 1], 'bo-')
plt.plot(S2[:, 0], S2[:, 1], 'ro-')

plt.axis('equal')
plt.xlim(-2, 2)
plt.ylim(-2, 2)

plt.show()
