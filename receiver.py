#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
#import adi


samples = np.fromfile('ask_in_noise.iq', np.complex64)

fig, ax1 = plt.subplots()
ax1.plot(samples)
plt.show()