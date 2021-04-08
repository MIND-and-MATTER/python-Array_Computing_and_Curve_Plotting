# Fill arrays; vectorized version

import numpy as np

def h(x):
  num = np.exp(-(x*x)/2)
  den = np.sqrt(2*np.pi)
  h = num / den
  return h

xlist = np.linspace(-4, 4, 41)
ylist = h(xlist)

print(xlist, ylist)
