import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')

print('sampling rate:', sampling_rate)  # frequency (sample per second)
print('data type:', data.dtype)
print('data shape:', data.shape)

N, no_channels = data.shape  # signal length and no. of channels

print('signal length:', N)

channel0 = data[:, 0]
channel1 = data[:, 1]

data_new = np.flip(data)

scipy.io.wavfile.write('output4.wav', sampling_rate, data_new)
