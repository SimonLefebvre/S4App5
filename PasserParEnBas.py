import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wave

samplingRate, dataGuitare = wave.read('AudioFiles/note_guitare_LAd.wav')
y_guitar = np.fft.fft(dataGuitare)
x_guitar = np.fft.fftfreq(len(y_guitar), (1.0 / samplingRate))

K = 885
a = 1/K

lenght = len(y_guitar)
samp = 1.0 / samplingRate

start = 0
stop = np.pi*2
step = stop / len(y_guitar)

w = np.arange(start,stop, step)

H_m = (a * np.sin(K*w/2))/(np.sin(w/2))
H_m[0] = a*K
print('H_m')
print(len(H_m))
print('w')
print(len(w))

plt.subplot(3,1,1)
plt.stem(w,H_m)
plt.subplot(3,1,2)
plt.plot(x_guitar, np.abs(y_guitar))


T_guitare_FREQ = H_m * y_guitar;
plt.subplot(3,1,3)
plt.plot(x_guitar,np.abs(T_guitare_FREQ))
plt.show()


T_guitare_temp = np.fft.ifft(T_guitare_FREQ)




plt.plot(T_guitare_temp)
plt.show()

wave.write("MaGuitarefenetrer.wav", samplingRate, T_guitare_temp.astype(np.int16))


