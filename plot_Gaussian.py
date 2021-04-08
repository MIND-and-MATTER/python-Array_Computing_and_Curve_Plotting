# Plot a function

import matplotlib
import matplotlib.pyplot as plt
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

fig, ax = plt.subplots()
ax.plot(xlist, hlist)

ax.set(xlabel="X axis", ylabel="y axis", title="Gaussian plot")
ax.grid()

fig.savefig("test.png")
plt.show()
