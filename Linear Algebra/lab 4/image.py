import imageio
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('macosx')

I = imageio.imread('nasir-al-mulk-gray.jpg')    # 0 = black, 255 = white

print('I=\n', I)
print('I.dtype=\n', I.dtype)  # uint8
print('I.shape=\n', I.shape)  # (853, 1280)  853 * 1280 = 1091840

plt.imshow(I, cmap='gray')
plt.show()

plt.imshow(I.T, cmap='gray')
plt.show()

plt.imshow(I[100:400, 300:600], cmap='gray')
plt.show()
