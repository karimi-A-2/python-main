import numpy as np
import scipy.io.wavfile

sampling_rate, data = scipy.io.wavfile.read('voice1.wav')

print('sampling rate:', sampling_rate)  # frequency (sample per second)
print('data type:', data.dtype)
print('data shape:', data.shape)

N, no_channels = data.shape  # signal length and no. of channels

print('signal length:', N)

data_new = np.flip(data)

scipy.io.wavfile.write('output4.wav', sampling_rate, data_new)
