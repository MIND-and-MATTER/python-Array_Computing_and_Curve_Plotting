# Animate a wave packet

import numpy as np
from numpy import exp, sin, pi
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


dist = np.linspace(-6, 6, 250)
t = np.linspace(-1,1, 250)
ampletude =  exp(-(dist-3*t)**2) * sin(3*pi*((dist-3*t)))

fig = plt.figure()
lines = plt.plot(dist,t)
plt.axis([dist[0], dist[-1], -1,1])
plt.xlabel('Linear Distance')
plt.ylabel('Ampletude')


def frame(stills):
  t = stills
  y = exp(-(dist-3*t)**2) * sin(3*pi*((dist-3*t)))
  lines[0].set_ydata(y)
  return lines


anim = FuncAnimation(fig, frame, frames = t*5, interval = 50)
anim.save("wave.gif","imagemagick")

