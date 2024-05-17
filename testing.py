#!/usr/bin/python3

import pdb
import numpy as np

array = np.array([1, 2, 3, 4, 5])

pad_width = (50, 50)
padded_array = np.pad(array, pad_width, mode='constant', constant_values=0)

for elem in padded_array:
    print(elem)
