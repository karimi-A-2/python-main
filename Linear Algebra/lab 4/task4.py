import imageio
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('macosx')

G = imageio.imread('nasir-al-mulk-gray.jpg')
I = imageio.imread('nasir-al-mulk.jpg')

G = np.stack((G,) * 3, axis=-1)
for alpha in np.linspace(0, 1, 20):
    J = np.uint8(alpha * I + (1 - alpha) * G)
    
    plt.imshow(J)
    plt.draw()
    plt.pause(.1)

plt.show()
