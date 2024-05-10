#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import adi

signal = np.fromfile('signal_with_noise.iq', np.complex64)
frequency = 85
sample_rate = 300
symbol_rate = 1

def signal_ask_demodulation(signal, frequency, sample_rate, symbol_rate):
    """
    Demodulate a signal using ASK demodulation

    Parameters:
    signal (np.array): The signal to demodulate
    frequency (int): The frequency of the carrier wave
    sample_rate (int): The sample rate of the signal
    symbol_rate (int): The symbol rate of the signal

    Returns:
    samples (np.array): The demodulated samples
    """
    samples = None
    magnitudes = np.abs(signal)
    threshold = .25
    samples_symbol = sample_rate // symbol_rate

    bits = [1 if m > threshold else 0 for m in magnitudes]
    decoded_bits = []
    for i in range(0, len(bits), samples_symbol):
        chunk = bits[i:i+samples_symbol]
        if np.sum(chunk) > samples_symbol // 2:
            decoded_bits.append(1)
        else:
            decoded_bits.append(0)

    return decoded_bits

def signal_to_bits(signal):
    """
    Convert a signal to bits
    
    Parameters:
    signal (np.array): The signal to convert to bits

    bits (list): The bits that were decoded from the signal
    """
    magnitudes = np.abs(signal)
    
    threshold = .25 # don't hard code this

    bits = [1 if m > threshold else 0 for m in magnitudes]
    decoded_bits = []
    for i in range(0, len(bits), 25):
        chunk = bits[i:i+25]
        if np.sum(chunk) > 12:
            decoded_bits.append(1)
        else:
            decoded_bits.append(0)
    return decoded_bits 

def bits_to_string(bits):
    """
    Convert a list of bits to a string

    Parameters:
    bits (list): The list of bits to convert to a string

    Returns:
    string (str): The string that was decoded from the bits
    """
    string = ""
    
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        byte = "".join([str(b) for b in byte])
        byte = int(byte, 2)
        string += chr(byte)

    return string

bits = signal_ask_demodulation(signal, frequency, sample_rate, symbol_rate)
message = bits_to_string(bits)
print(message)
#fig, ax1 = plt.subplots()
#fig, ax2 = plt.subplots()
#fig, ax3 = plt.subplots()

#ax1.plot(samples, "-*")
#ax2.plot(magnitudes, "-*")
#ax3.plot(bits, "-*")

#plt.show()
