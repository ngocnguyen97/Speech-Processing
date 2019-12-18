import scipy as scp
from scipy import signal
from numpy.fft import fft, ifft
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read

def configFilter(data, a):
	out = []
	for i in range(1, len(data), 1):
		out.append(data[i] - a * data[i-1])
	return out

fig, (ax1, ax2, ax3, ax4, ax5) = pl.subplots(5 , 1 , sharex=False)

rate, data = read('e.wav')

print(rate)
sizecut = 256
start = 5000
#start = 100

ax1.plot(data)
ax1.set_title('Original')

for i in [0, 0.98]:
	sg = data[start :start + sizecut]
	#sg = data[start :start + sizecut] - 0.95 * data[start - 1:start - 1 + sizecut]
	sg = configFilter(sg, i)

	ax2.plot(sg)
	ax2.set_title('After Adjust Filter')

	sg = sg * np.hamming(sizecut-1)

	sg = np.abs(fft(sg))

	sg = np.log(sg) 
	ax4.plot(sg[0:len(sg)//2])

	#ax3.plot(sg[0:sizecut//2])

	#sg = sg[0:int(sizecut/2)]

	sg = ifft(sg).real
	ax5.plot(sg)


	#ax4.plot(np.abs(sg))
	#ax4.set_title('Inverse log fft')
		
	sg[30:] = 0

	sg = fft(sg)
	sg = sg[0:len(sg)//2]
	#ax3.plot(sg)
	ax3.plot(sg)
	ax4.plot(sg)

	print("formant %f" % i)
	for i in range(1,len(sg)-1):
		if sg[i] > sg[i-1] and sg[i] > sg[i+1] : 
			print(i*1.0 /sizecut * rate)


#ax6.set_ylim([0, maxx])

	
pl.show()
 

