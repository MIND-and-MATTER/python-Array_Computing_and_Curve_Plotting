# Fill lists with function values

import numpy as np
import math as m

def h(x):
  num = m.exp(-(x*x)/2)
  den = m.sqrt(2*m.pi)
  h = num / den
  return h


xlist = np.linspace(-4, 4, 41)
hlist = []

for i in xlist:
  hlist.append(h(i))

print(xlist)
print(hlist)