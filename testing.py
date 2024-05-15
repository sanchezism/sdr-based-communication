#!/usr/bin/python3

import pdb
import numpy as np

pdb.set_trace()
array = np.array([1, 2, 3, 4, 5])
print(array)
num_zeros = 5
array = np.pad(array, (num_zeros, 0+0j), 'constant', constant_values=(0,))
print(array)
