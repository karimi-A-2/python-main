import imageio
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

matplotlib.use('macosx')

I = imageio.imread('nasir-al-mulk-gray.jpg')

row_0 = np.concatenate((I, np.flip(I, 1)), 1)
I_f = np.flip(I, 0)
row_1 = np.concatenate((I_f, np.flip(I_f, 1)), 1)

result = np.concatenate((row_0, row_1))
plt.imshow(result, cmap='gray')
plt.show()

# I I_1
# If If_I1
