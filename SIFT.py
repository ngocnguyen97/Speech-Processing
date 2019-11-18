from scikits.talkbox.linpred.levinson_lpc import lpc
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read

rate, data = read('Xe.wav')
fig, ax = pl.subplots(5 , 1 , sharex=False)

start = 6000
N = 256
K = 128

def Az(data, n, a):
	re = 0
	for i in range(0, len(a)):
		re += a[i]*data[n - i]
	return re

def AzAll(data, start, size, a):
	re = []
	for i in range(0, size):
		re.append(Az(data, start + i, a))
	return re

def R(dat):
	kq = []
	data1 = np.arange(len(dat))
	for i in range(len(dat)):
		if abs(dat[i]) < 3000:
			data1[i] = 0;
		else:
			data1[i] = dat[i]
	for i in range(0, K, 1):
		x = 0
		for j in range(0, N - i, 1):
			x = x + data1[j] * data1[j + i]
		kq.append(x)
	return kq


win = data[start:start + N]

ax[0].plot(win)

a, e, k = lpc(win, 4, -1)

win = AzAll(data, start, N, a)
ax[1].plot(win)
Rwin = R(win)

ax[2].plot(Rwin)

F0 = []
xplot4 = []

for i in range(0, len(data) - N, N ):
	win1 = data[i:i+N]
	a, e, k = lpc(win1, 4, -1)
	win2 = AzAll(data, i, N, a)
	Rwin = R(win2)
	T0 = 0
	for j in range(20, len(Rwin), 1):
		if Rwin[j] == max(Rwin[30:100]):
			T0 = j
	f = rate * 1.0 / T0
	if f > 150:
		F0.append(f)
		xplot4.append(i * 1.0/ rate)

print(F0)
ax[3].scatter(xplot4 ,F0)

ax[3].set_xlim([0, len(data) * 1.0 / rate])

ax[3].set_ylim([0, max(F0)])

ax[4].plot(np.arange(len(data)) * 1.0 / rate, data)
ax[4].set_xlim([0, len(data) * 1.0 / rate])

pl.show()