# Fill arrays; loop version

import numpy as np
import math as m


def h(x):
  num = m.exp(-(x*x)/2)
  den = m.sqrt(2*m.pi)
  h = num / den
  return h

xlist = np.linspace(-4, 4, 41)
x = np.empty([len(xlist)])
y = np.empty([len(xlist)])

for i in range(0, 41):
  x[i] = xlist[i]
  y[i] = h(xlist[i])
  
for i, j in zip(x,y):
  print(i, j)
