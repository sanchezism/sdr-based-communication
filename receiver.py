#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import adi

signal = np.fromfile('signal_with_noise.iq', np.complex64)

def signal_to_bits(signal):
    """
    Convert a signal to bits
    
    Parameters:
    signal (np.array): The signal to convert to bits

    bits (list): The bits that were decoded from the signal
    """
    magnitudes = np.abs(signal)
    
    threshold = .25

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

bits = signal_to_bits(signal)
string = bits_to_string(bits)
print(string)

#fig, ax1 = plt.subplots()
#fig, ax2 = plt.subplots()
#fig, ax3 = plt.subplots()

#ax1.plot(samples.real)
#ax2.plot(magnitudes)
#ax3.plot(bits, "-*")

#plt.show()
