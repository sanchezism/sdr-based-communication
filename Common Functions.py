#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

char = "Hello"

bit_map = {-1-1j: '00', -1+1j: '01', 1-1j: '10', 1+1j: '11'}
bit_map_reverse = {value: key for key, value in bit_map.items()}
   

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

    
    fig, ax1 = plt.subplots()
    ax1.plot(np.real(two_bits_to_complex), np.imag(two_bits_to_complex), '.')
    plt.show()


def qpsk_demodulate_symbols(complex_symbols):
    symbols_to_bit_pairs = [bit_map[symbol] for symbol in complex_symbols]
    bits_as_string = "".join(symbols_to_bit_pairs)
    byte_chunks = [bits_as_string[i:i+8] for i in range(0, len(bits_as_string), 8)]
    char_lst = [chr(int(byte, 2)) for byte in byte_chunks]
    chars = "".join(char_lst)

    return chars

iq_samps = qpsk_modulate_text(char)
print(iq_samps)

demodulated_result = qpsk_demodulate_symbols(iq_samps)
print(demodulated_result)
#fig, ax1 = plt.subplots()
#ax1.plot(np.real(iq_samps), np.imag(iq_samps), '.')
#plt.show()
         
