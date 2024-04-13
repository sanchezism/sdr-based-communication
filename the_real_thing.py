#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import adi

# Create a carrier wave
def create_carrier_wave(frequency, sample_rate, duration, phase):

    f = frequency # cycles / sec
    Fs = sample_rate # samples / sec also seen as Fs
    T = duration # sec aslo seen as T
    Ts = 1 / Fs # sample interval also seen as Ts
    t = np.arange(0, T, Ts) # time vector
    theta = phase # phase shift in radians



    carrier = np.sin(2 * np.pi * frequency * t + phase)


def qpsk_modulate_text(text):                                
    text_to_byte = [format(ord(char), '08b') for char in text]                                
    bits = [bit for byte in text_to_byte for bit in byte]                                
    two_bits_to_complex = np.array([bit_map_reverse[f'{bits[i]}{bits[i+1]}'] for i in range(0, len(bits), 2)])                                
    return two_bits_to_complex

# QPSK bit mapping to get complex numbers
bit_map = {-1-1j: '00', -1+1j: '01', 1-1j: '10', 1+1j: '11'}                                
bit_map_reverse = {value: key for key, value in bit_map.items()}

# Message to be transmitted
chars = "ISMAEL SANCHEZ IS COOL"

# Modulate the text
symbols = qpsk_modulate_text(chars)

# Configure a carrier wave
f = 10 # cycles / sec
Fs = 1000 # samples / sec also seen as Fs
Ts = 1 / Fs # sample interval also seen as Ts
T = 1 # sec
t = np.arange(0, T, Ts) # time vector


samples_per_symbol = Fs / len(symbols)
repeated_symbols = np.repeat(symbols, samples_per_symbol)
theta = repeated_symbols # phase shift in radians

if t.size > len(repeated_symbols):
    padding = np.zeros(t.size - len(theta))
    theta = np.concatenate((repeated_symbols, padding))

print(samples_per_symbol)

# Create a carrier wave with the modulation scheme
carrier = np.sin(2 * np.pi * f * t + np.angle(theta)) 


fig, ax1 = plt.subplots()
ax1.plot(t, carrier)
plt.show()
