import imageio
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('macosx')

I = imageio.imread('nasir-al-mulk.jpg')

for alpha in np.linspace(0, 1, 20):
    J = np.uint8(I * [np.sin(alpha), np.sin(alpha + np.pi / 4), np.sin(alpha + np.pi / 2)])
    
    plt.imshow(J)
    plt.draw()
    plt.pause(.1)

plt.show()
