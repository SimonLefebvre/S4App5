import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wave

samplingRate, data = wave.read('AudioFiles/note_basson_plus_sinus_1000_Hz.wav')
y_basson = np.fft.fft(data)
x_basson = np.fft.fftfreq(len(y_basson), (1.0 / samplingRate))

samplingRate, data = wave.read('AudioFiles/note_guitare_LAd.wav')
y_guitar = np.fft.fft(data)
x_guitar = np.fft.fftfreq(len(y_guitar), (1.0 / samplingRate))

plt.subplot(3, 1, 1)
plt.title('fft La# Guitar')
plt.plot(x_guitar, np.abs(y_guitar))

plt.subplot(3, 1, 2)
plt.title('fft Basson')
plt.plot(x_basson, np.abs(y_basson))
#plt.show()

# Filtre coupe bande

fc = 1000
N_h = 1024
w0 = 1000 * 2 * np.pi

n_h = np.arange(-N_h / 2, N_h / 2)
K_h = 2 * (fc / samplingRate * N_h) + 1
h = (1 / N_h) * (np.sin(np.pi * n_h * K_h / N_h)) / (np.sin(np.pi * n_h * N_h)+1e-20)
H = np.fft.fftshift(np.fft.fft(h))
plt.subplot(3, 1, 3)
plt.plot(h)
#plt.show()

N3 = h.shape[0]
N4 = y_basson.shape[0]
N5 = N3+N4-1

rep = np.convolve(h, data)
y_rep = np.fft.fft(rep)
x_rep = np.fft.fftfreq(len(y_rep), (1.0 / samplingRate))

plt.subplot(3, 1, 3)
plt.title('fft basson apres filtre')
#plt.plot(x_rep, np.abs(y_rep))
plt.show()
