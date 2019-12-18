import scipy as scp
from scipy import signal
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read

fig, ax = pl.subplots(4 , 1 , sharex=False)

u = 255
xmax = 1
F = 100
Fs = 1000
N = 1000

def C(x):
	#xmax = np.max(x)
	y = np.sign(x)*np.log(1+u*np.abs(x)/xmax) / np.log(1+u)
	return y

def E(y):
	p = np.sign(y)*((1+u)**np.abs(y) - 1) / u
	return p


x = xmax*np.sin(2*np.pi * np.arange(N) * F / Fs)
#x = (np.arange(N) - 10) * (np.arange(N) - 40) * (np.arange(N) - 80)



ax[0].plot(x)

y = fft(x)
ax[1].plot(y)


#pl.xticks(np.arange(N))

pl.show()