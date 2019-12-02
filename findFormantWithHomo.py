import scipy as scp
from scipy import signal
from numpy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read

def configFilter(data):
	out = []
	for i in range(1, len(data), 1):
		out.append(data[i] - 0.98 * data[i-1])
	return out

fig, (ax1, ax2, ax3, ax4) = pl.subplots(4 , 1 , sharex=False)

rate, data = read('Xe.wav')


sizecut = 256
start = 6000
#start = 100

ax1.plot(data[start :start + sizecut])
ax1.set_title('Original')

sg = data[start :start + sizecut] - 0.95 * data[start - 1:start - 1 + sizecut]
# sg = configFilter(sg)

ax2.plot(sg)
ax2.set_title('After Adjust Filter')

sg = sg * np.hamming(sizecut)

sg = np.abs(fft(sg))

sg = np.log(sg) 
ax4.plot(sg[0:len(sg)//2])

#ax3.plot(sg[0:sizecut//2])

#sg = sg[0:int(sizecut/2)]

sg = ifft(sg).real

#ax4.plot(np.abs(sg))
#ax4.set_title('Inverse log fft')
	
sg[20:] = 0

sg = fft(sg)
sg = sg[0:len(sg)//2]
#ax3.plot(sg)
ax3.plot(sg)
ax4.plot(sg)


for i in range(1,len(sg)-1):
	if sg[i] > sg[i-1] and sg[i] > sg[i+1] : 
		print(i*1.0 /256 * rate)


#ax6.set_ylim([0, maxx])

	
pl.show()
 

