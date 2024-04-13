#!/usr/bin/python3

# April 12, 2024

import numpy as np
import matplotlib.pyplot as plt
import adi

# Create a message signal that can be transmitted
char = "Hello"

center_freq = 900 # Hz
duration = 10 # seconds
sample_rate = 1e6 # samples per second (Hz)
data_rate = 1 # symbols per second

# Configure the PlutoSDR
sdr = adi.Pluto("ip:192.168.2.1")
sdr.sample_rate = int(sample_rate)
sdr.tx_rf_bandwidth = int(sample_rate)
sdr.tx_lo = int(center_freq)
sdr.tx_hardwaregain_chan0 = -50

# Modulate the signal using QPSK
carrier_signal = np.exp(2j * np.pi * center_freq * t)
rf_signal = carrier_signal * baseband



number_of_symbols = (data_rate * duration)
data = np.random.randint(0, 2, number_of_symbols)


t = np.arange(0, duration, 1/sample_rate) # 1/sample_rate is the period (time between samples)
t_symbol = np.arange(0, 1 / data_rate, 1 / sample_rate)


signal = np.sin(2 * np.pi * freq_center * t_symbol)

modulated_signal = np.repeat(data, len(t_symbol)) * np.tile(signal, number_of_symbols)

for i in range(100):
    sdr.tx(modulated_signal)

fig, ax1 = plt.subplots()
fig, ax2 = plt.subplots()
#fig, ax3 = plt.subplots()

ax1.plot(t_symbol, signal, '-')
ax2.plot(t, modulated_signal, '-')
#ax3.plot(t, signal, '-')

plt.show()

num_symbols = 10
N = 10 # samples per symbol (Hz) I think this is also the sampling rate

symbols = 2 * np.random.randint(0, 2, num_symbols) - 1
print(f'symbols to be transmitted: {symbols}')

samples_per_symbol = np.repeat(symbols, N)
print(f'samples per symbol: {samples_per_symbol}')


