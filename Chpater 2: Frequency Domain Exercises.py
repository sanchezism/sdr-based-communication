# Chpater 2: Frequency Domain Exercises

import numpy as np
import matplotlib.pyplot as plt

Fs = 1 # Hz
N = 100 # number of points to simulate, and our FFT size

# Create a simple sine wave signal 
# in the time domain at 0.15 Hz and a sample rate of 1 Hz
t = np.arange(N)
s = np.sin(.15*2*np.pi*t)

# FFT of the time domain frequency (list of complex numbers)
S = np.fft.fftshift(np.fft.fft(s))

S_mag = np.abs(S)
S_pahse = np.angle(S)
f = np.arange(Fs/-2, Fs/2, Fs/N)

plt.figure(0)
plt.plot(t, S_mag, '.-')
plt.figure(1)
plt.plot(t, S_pahse, ".-")
plt.figure(2)
plt.plot(s)
plt.show()