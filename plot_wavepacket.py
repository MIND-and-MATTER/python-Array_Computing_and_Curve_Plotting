# Plot a wave packet

import numpy
from numpy import sin, pi, exp
import matplotlib.pyplot as plt

distance = numpy.linspace(-4, 4, 100000)

ampletude = exp(-(distance)**2) * sin(3*pi*((distance)))

plt.plot(distance,ampletude)
plt.xlabel('Linear Distance')
plt.ylabel('Ampletude')
plt.show()