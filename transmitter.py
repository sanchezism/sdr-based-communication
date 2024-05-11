#!/usr/bin/python3

import pdb
import numpy as np
import matplotlib.pyplot as plt
import adi
import time

def ascii_to_bits(ascii_string):
    """
    Convert an ASCII string to a list of bits.

    Parameters:
    - ascii_string (string): the ASCII string to convert

    Returns:
    - bits (numpy array): the list of bits
    """

    bits = np.array([], dtype=int)
    preamble = np.array([1, 1, 0, 0, 1, 1, 0, 0, 1, 1], dtype=int)
    for char in ascii_string:
        bits = np.append(bits, np.array([int(bit) for bit in format(ord(char), '08b')]))
    
    bits = np.concatenate((preamble, bits))
    return bits


def ask_modulation(bits, frequency, sample_rate=None, symbol_rate=None):
    """
    Perform ASK modulation on a list of bits.

    Parameters:
    - bits (numpy array): the list of bits to modulate
    - frequency (int): the carrier frequency in Hz
    - sample_rate (int): the sample rate in Hz
    - symbol_duration (int, optional): the duration of each symbol in seconds

    Returns:
    - modulated_signal (numpy array): the modulated signal
    - t (numpy array): the time vector
    """
    if sample_rate is None:
        sample_rate = frequency * 10
    if symbol_rate is None:
        symbol_rate = 1


    #if symbol_duration is None:
    #    symbol_duration = 1 / 10 * frequency # don't need
    # Calculate the number of samples per symbol
    samples_per_symbol = int(sample_rate / symbol_rate)
    
    # Create the time vector
    t = np.arange(0, len(bits) * samples_per_symbol) / sample_rate
    
    # Create the carrier signal
    #carrier = np.sin(2 * np.pi * frequency * t + np.pi * np.repeat(bits, samples_per_symbol))
    carrier = np.repeat(bits, samples_per_symbol) * np.cos(2 * np.pi * frequency * t) # ASK
    return carrier, t

# characters to send
#pdb.set_trace()
char = "Hello, Ismael! This is Bo"
frequency = 200
sample_rate = 500 
symbol_rate = 100
carrier, t = ask_modulation(ascii_to_bits(char), frequency, sample_rate, symbol_rate)


# Generate noise and add it to the signal
std_dev = 0.1
noise = np.random.normal(0, std_dev, len(carrier))
signal_with_noise = carrier + noise
signal_with_noise = np.pad(signal_with_noise, (40, 0), 'constant', constant_values=(0,))
signal_with_noise = signal_with_noise.astype(np.complex64)

#pdb.set_trace()
#for i in range(500):
#    print(signal_with_noise[i].real, signal_with_noise[i].imag)

signal_with_noise.tofile('signal_with_noise.iq')

# plot the time domain signal
fig, ax1 = plt.subplots()
ax1.plot(t, carrier, '-')

# plot the frequency domain signal
f = np.fft.fftshift(np.fft.fftfreq(len(carrier), 1 / sample_rate))
fig, ax2 = plt.subplots()
S = np.fft.fftshift(np.fft.fft(carrier))
ax2.plot(f, np.real(S), '-')

fig, ax3 = plt.subplots()
ax3.plot(signal_with_noise, '-')

plt.show()
#def main():
#    # Create a PlutoSDR object
#    sdr = adi.Pluto("ip:192.168.2.1")
#
#    # Set the sample rate and frequency
#    sample_rate = 1e6
#    frequency = 915e6
#    bandwidth = 20e6
#
#    # Configure the PlutoSDR
#    sdr.sample_rate = int(sample_rate)
#    sdr.tx_rf_bandwidth = int(bandwidth)
#    sdr.tx_lo = int(frequency)
#    sdr.tx_hardwaregain_chan0 = -20
#    start_time = time.time()
#    
#    while True:
#        receive_or_transmit = input("Do you want to transmit or receive? (t/r): ")
#        if receive_or_transmit == 't':
#            # Get the user input and convert it to a list of bits
#            user_input = input("user 1: ")
#            bits = ascii_to_bits(user_input)
#
#            # Perform PSK modulation
#            f = 100
#            Fs = 10000
#            modulated_signal, t = ask_modulation(bits, f, Fs)
#
#            # Transmit the modulated signal
#            modulated_signal *= 2**14
#            for i in range(100):
#                sdr.tx(modulated_signal)
#            
#            break
#        elif receive_or_transmit == 'r':
#            sdr.gain_control_mode_chan0 = 'manual'
#            sdr.rx_hardwaregain_chan0 = 70.0
#            sdr.rx_lo = int(frequency)
#            sdr.rx_rf_bandwidth = int(bandwidth)
#            sdr.rx_buffer_size = 10000
#
#            samples = sdr.rx()
#            print(samples[0:20])
#
#
#
#if __name__ == "__main__":
#    main()
