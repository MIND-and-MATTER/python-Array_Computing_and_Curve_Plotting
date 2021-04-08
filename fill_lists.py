# Fill lists with function values

import numpy as np

def h(x):
  num = np.exp(-(x*x)/2)
  den = np.sqrt(2*np.pi)
  h = num / den
  return h


xlist = np.linspace(-4, 4, 41)
hlist = []

for i in xlist:
  hlist.append(h(i))

print(xlist)
print(hlist)