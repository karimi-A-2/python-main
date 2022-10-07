import numpy as np
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

x = np.arange(0, 2 * np.pi, 0.1)
x
y = np.cos(x)
y
plt.plot(x, y)
plt.show()
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()
