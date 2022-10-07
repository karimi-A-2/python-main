import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')

N, no_channels = data.shape  # signal length and no. of channels

channel0 = data[:, 0]
channel1 = data[:, 1]

x = np.arange(N)

plt.plot(x, channel0)
plt.plot(x, channel1)
plt.show()

plt.plot(x, data)
plt.show()

scale = 2 ** np.linspace(-2, 4, N)
scale.shape = (N, 1)
data_new = np.int16(scale * data)

plt.plot(x, data)
plt.plot(x, data_new)
plt.show()
