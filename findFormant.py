from scikits.talkbox.linpred.levinson_lpc import lpc
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read

def configFilter(data):
	out = []
	for i in range(1, len(data), 1):
		out.append(data[i] - 0.98 * data[i-1])
	return np.array(out)

rate, data = read('e.wav')
fig, (ax1, ax2, ax3, ax4) = pl.subplots(4 , 1 , sharex=False)

size = 512
win = data[5000:5000 + size]
ax1.plot(win)
win = configFilter(win)
ax2.plot(win)

a, e, k = lpc(win, 20, -1)

print(k)

data1 = np.zeros(size)
data1[:len(a)] = a

data1 = fft(data1)

data1 = - np.log(np.abs(data1))

for i in range(1,len(data1)/2):
	if data1[i] > data1[i-1] and data1[i] > data1[i+1] : 
		print(i*1.0 /size * rate)

ax3.plot(data1[0:len(data1)/2])
ax4.plot(np.log(fft((win))[0:size/2]))
pl.show()

# tinh fft cua ai(1, a1, a2, ... ap, 0,0,..) (kich thuoc 256) -> A(e^jw) -> lay bien do |A|
# -lg ||