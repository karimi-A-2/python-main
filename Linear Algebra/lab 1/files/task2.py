import matplotlib
import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt
matplotlib.use('macosx')

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')

print('sampling rate:', sampling_rate)  # frequency (sample per second)
print('data type:', data.dtype)
print('data shape:', data.shape)

N, no_channels = data.shape  # signal length and no. of channels

print('signal length:', N)

channel0 = data[:, 0]
channel1 = data[:, 1]

scale = 2 ** np.linspace(-2, 4, N)

plt.plot(np.arange(N), scale)
plt.show()

print('shape_old:', scale.shape)
scale.shape = (N, 1)
print('shape_new:', scale.shape)

data_new = np.int16(scale * data)

scipy.io.wavfile.write('output2.wav', sampling_rate * 2, data_new)
scipy.io.wavfile.write('output3.wav', sampling_rate // 2, data_new)
