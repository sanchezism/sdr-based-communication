#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import adi

"""
Function to modulate text to complex symbols

@params: text - string of text to be modulated
@return: two_bits_to_complex - list of complex symbols modulated from the text provided
"""
def qpsk_modulate_text(text):
    text_to_byte = [format(ord(char), '08b') for char in text]
    bits = [bit for byte in text_to_byte for bit in byte]
    two_bits_to_complex = np.array([bit_map_reverse[f'{bits[i]}{bits[i+1]}'] for i in range(0, len(bits), 2)])
    return two_bits_to_complex
    
"""
Function to demodulate complex symbols to text

@params: complex_symbols - list of complex symbols to be demodulated
@return: chars - string of text demodulated from the complex symbols provided
"""
def qpsk_demodulate_symbols(complex_symbols):
    symbols_to_bit_pairs = [bit_map[symbol] for symbol in complex_symbols]
    bits_as_string = "".join(symbols_to_bit_pairs)
    byte_chunks = [bits_as_string[i:i+8] for i in range(0, len(bits_as_string), 8)]
    char_lst = [chr(int(byte, 2)) for byte in byte_chunks]
    chars = "".join(char_lst)

    return chars

char = "Hello"

bit_map = {-1-1j: '00', -1+1j: '01', 1-1j: '10', 1+1j: '11'}
bit_map_reverse = {value: key for key, value in bit_map.items()}




frequency = 10 # Hz
sample_rate = 1000 # (samples per second)
T = 1 / sample_rate # time between samples
duration = 1 # second
t = np.arange(0, duration, T) # time vector 

carrier = np.cos(2 * np.pi * frequency * t) # carrier signal

fig, ax1 = plt.subplots()
ax1.plot(t, carrier)
plt.show()
#
#message_in_complex = qpsk_modulate_text(char)
#
#print(message_in_complex)
