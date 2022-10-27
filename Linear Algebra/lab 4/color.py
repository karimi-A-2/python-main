import imageio
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('macosx')

I = imageio.imread('nasir-al-mulk.jpg')

print('I.shape=', I.shape)  # (853, 1280, 3)

plt.imshow(I)
plt.show()
