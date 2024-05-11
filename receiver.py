#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import adi
from scipy.signal import correlate
import pdb


def preamble_to_signal(preamble, frequency, sample_rate, symbol_rate):
    """
    Convert a preamble to a signal

    Parameters:
    preamble (list): The preamble to convert to a signal
    frequency (int): The frequency of the carrier wave
    sample_rate (int): The sample rate of the signal
    symbol_rate (int): The symbol rate of the signal

    Returns:
    signal (np.array): The signal that was generated from the preamble
    """
    samples_per_symbol = int(sample_rate / symbol_rate)

    t = np.arange(0, len(preamble) * samples_per_symbol) / sample_rate
    carrier = np.repeat(preamble, samples_per_symbol) * np.cos(2 * np.pi * frequency * t)

    return carrier

def correlation(signal, preamble):
    """
    Correlate a signal with a preamble

    Parameters:
    signal (np.array): The signal to correlate
    preamble (list): The preamble to correlate with

    Returns:
    index (int): The index of the preamble in the signal
    """
    correlation_output = np.correlate(signal, preamble, mode="valid")
    peak_index = np.argmax(correlation_output)
    peak_value = correlation_output[peak_index]

    #if peak_value > threshold:
    #    print(f"Preamble detected at index {peak_index - len(preamble) + 1}")
    
    return peak_index
    
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
    samples_per_symbol = sample_rate // symbol_rate

    bits = [1 if m > threshold else 0 for m in magnitudes]
    decoded_bits = []
    for i in range(0, len(bits), samples_per_symbol):
        chunk = bits[i:i+samples_per_symbol]
        if np.sum(chunk) > samples_per_symbol // 2:
            decoded_bits.append(1)
        else:
            decoded_bits.append(0)

    return decoded_bits

#def signal_to_bits(signal):
#    """
#    Convert a signal to bits
#    
#    Parameters:
#    signal (np.array): The signal to convert to bits
#
#    bits (list): The bits that were decoded from the signal
#    """
#    magnitudes = np.abs(signal)
#    
#    threshold = .25 # don't hard code this
#
#    bits = [1 if m > threshold else 0 for m in magnitudes]
#    decoded_bits = []
#    for i in range(0, len(bits), 25):
#        chunk = bits[i:i+25]
#        if np.sum(chunk) > 12:
#            decoded_bits.append(1)
#        else:
#            decoded_bits.append(0)
#    return decoded_bits 

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

#pdb.set_trace()
signal = np.fromfile('signal_with_noise.iq', np.complex64)
frequency = 200
sample_rate = 500
symbol_rate = 100
samples_per_symbol = sample_rate // symbol_rate

preamble_bits = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
preamble_signal = preamble_to_signal(preamble_bits, frequency, sample_rate, symbol_rate)

start_of_message = correlation(signal, preamble_signal) + (len(preamble_bits) * samples_per_symbol)
signal = signal[start_of_message:]

bits = signal_ask_demodulation(signal, frequency, sample_rate, symbol_rate)
message = bits_to_string(bits)

string_bits = ''.join([str(b) for b in bits])
#print(string_bits)
print(message)



#fig, ax1 = plt.subplots()
#fig, ax2 = plt.subplots()
#fig, ax3 = plt.subplots()
#fig, ax4 = plt.subplots()
#fig, ax5 = plt.subplots()
#fig, ax6 = plt.subplots()

#ax1.plot(samples, "-*")
#ax2.plot(magnitudes, "-*")
#ax3.plot(bits, "-*")
#ax4.plot(corre, "*")
#ax5.plot(signal, "-*")
#ax6.plot(preamble_signal, "-*")

#plt.show()
