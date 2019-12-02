import scipy as scp
from scipy import signal
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read

fig, ax = pl.subplots(4 , 1 , sharex=True)

u = 255
xmax = 5
F = 10
Fs = 104
N = 100

def C(x):
	#xmax = np.max(x)
	y = np.sign(x)*np.log(1+u*np.abs(x)/xmax) / np.log(1+u)
	return y

def E(y):
	p = np.sign(y)*((1+u)**np.abs(y) - 1) / u
	return p


x = xmax*np.sin(2*np.pi * np.arange(N) * F / Fs)
#x = (np.arange(N) - 10) * (np.arange(N) - 40) * (np.arange(N) - 80)

y = C(x)
p = E(y)

ax[0].plot(x)
ax[1].plot(y)
ax[2].plot(p)

ax[3].plot(x)
ax[3].plot(y)
ax[3].plot(p)

pl.xticks(np.arange(N))

pl.show()