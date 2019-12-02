import scipy as scp
from scipy import signal
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read

fig, ax = pl.subplots(4 , 1 , sharex=True)

u = 255
A = 87.56
xmax = 5
F = 10
Fs = 100
N = 20

def zip(x):
	y = np.zeros(len(x))
	mx = np.max(x)
	for i in range(0,len(x)):
		if np.abs(x[i]) <= mx / A:
			y[i] = A*x[i] / (1 + np.log(A))
		else:
			y[i] = mx*(1 + np.log(A * np.abs(x[i]) / mx)) / (1 + np.log(A)) * np.sign(x[i])
	return y

def unzip(y):
	V = np.max(y)
	xd = np.zeros(len(y))
	for i in range(0,len(y)):
		if np.abs(y[i]) <= V / (1+np.log(A)):
			xd[i] = (1 + np.log(A)) * y[i] / A
		else:
			xd[i] = np.exp(np.abs(y[i]) * (1 + np.log(A)) / V - 1) * V / A * np.sign(y[i])
	return xd

x = xmax*np.sin(2*np.pi * np.arange(N) * F / Fs)
#x = (np.arange(N) - 10) * (np.arange(N) - 40) * (np.arange(N) - 80)

y = zip(x)
xd = unzip(y)

ax[0].plot(x)
ax[1].plot(y)
ax[2].plot(xd)

ax[3].plot(x)
ax[3].plot(y)
ax[3].plot(xd)


pl.xticks(np.arange(N))

pl.show()