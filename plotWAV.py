import scipy as scp
from scipy import signal
import numpy as np
import matplotlib.pyplot as pl

from scipy.io.wavfile import read

def sumsquare(x):
	kq = 0;
	for i in x:
		kq += i*i
	return kq

rate, data = read('khoosoothunhus.wav')

xplot = np.arange(len(data)) / rate

fig, (ax1, ax2, ax3) = pl.subplots(3 , 1 , sharex=False)

wd = 20
slide = 10

ax1.plot(xplot, data)


hm = signal.hamming(wd)

Wn = []
zrc = [0 for i in range(len(data))]

for i in range(slide, len(data)-slide-1, slide ):
	Sn = data[i-slide:i+slide]
	Wn.append(sumsquare(Sn*hm))
	for j in range(i-slide, i+slide, 1):
		if((data[j] > 0 and data[j+1] < 0) or (data[j] < 0 and data[j+1] > 0)):
			zrc[i]+= 1


ax2.plot(Wn)
ax3.plot(xplot, zrc)
	
pl.show()
 

