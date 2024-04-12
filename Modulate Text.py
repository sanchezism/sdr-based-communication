#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

num_symbols = 1000

x_int = np.random.randint(0, 4, num_symbols)
#for i in range(num_symbols):
#    print(x_int[i])

# add some noise
n = (np.random.randn(num_symbols) + 1j * np.random.randn(num_symbols)) / np.sqrt(2)
noise_power = 0.01
x_degress = x_int * 360 / 4.0 + 45
x_radians = x_degress * np.pi / 180.0
x_symbols = np.cos(x_radians) + 1j * np.sin(x_radians)
#phase_noise = np.random.randn(len(x_symbols)) * 0.1
# combine phase noise with AGWN
#r_phase_noise = x_symbols * np.exp(1j * phase_noise)
#r_phase_and_awgn = r_phase_noise + n * np.sqrt(noise_power)

bit_map = {-1-1j: '00', -1+1j: '01', 1-1j: '10', 1+1j: '11'}

ideal_points = np.array([-1-1j, -1+1j, 1-1j, 1+1j])


# find the closest ideal point to the first symbol
#all_ideal_points = min(ideal_points, key=lambda point: abs(symbol - point))

all_ideal_points = [min(ideal_points, key=lambda point: abs(symbol - point)) for symbol in x_symbols]

bits = [bit_map[point] for point in all_ideal_points]

bits_joined = bits

print(bits_joined)


#for i in range(num_symbols):
#    print(x_symbols[i])

#fig, ax1 = plt.subplots()
#fig, ax2 = plt.subplots()
#fig, ax3 = plt.subplots()

#ax1.plot(np.real(x_symbols), '.')
#ax2.plot(np.imag(x_symbols), '.')
#ax3.plot(np.real(r_phase_and_awgn), np.imag(r_phase_and_awgn), '.')

#ax1.grid(True)
#ax2.grid(True)
#ax3.grid(True)

#plt.show()
