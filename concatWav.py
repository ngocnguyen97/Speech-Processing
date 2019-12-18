import scipy as scp
from scipy import signal
from scipy.fftpack import fft, ifft
import numpy as np
import matplotlib.pyplot as pl
from scipy.io.wavfile import read
from scipy.io.wavfile import write

rate1, data1 = read('ta.wav')
rate2, data2 = read('am.wav')

cut = 2000
win = 100
print(rate1, rate2)

fig, ax = pl.subplots(4 , 1 , sharex=True)
ax[0].plot(data1)
ax[1].plot(data2)
max1 = np.max(data1[cut-win:cut+win]) - np.min(data1[cut-win:cut+win]) 
arg1 = np.argmax(data1[cut-win:cut+win])
max2 = np.max(data2[cut-win:cut+win]) - np.min(data2[cut-win:cut+win]) 
arg2 = np.argmax(data2[cut-win:cut+win])

data2 = data2 * (max1 / max2)
#ax[1].plot(data2)


data = np.array(list(data1[0:cut - win + arg1]) + list(data2[cut - win + arg2:]))

write('tam.wav', rate1, data)

print(cut - win + arg1)
ax[2].plot(data)
ax[3].plot(data1)
ax[3].plot(data2)
pl.show()