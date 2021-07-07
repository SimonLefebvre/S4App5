import matplotlib.pyplot as plt
import numpy as np

N= 256

n = np.arange(0, N, 1)
m = np.arange(-(N/2), N/2, 1)
w = 2*np.pi*m/128
win = np.hanning(N)

x_1 = np.sin(2*n*np.pi*0.1 + np.pi/4)
X_1 = np.fft.fftshift(np.fft.fft(x_1))
xw_1 = win * np.sin(2*n*np.pi*0.1 + np.pi/4)
Xw_1 = np.fft.fftshift(np.fft.fft(xw_1))

x_2 = np.cos(np.pi*n)
X_2 = np.fft.fftshift(np.fft.fft(x_2))

x_3 = np.zeros(N)
x_3[10] = 1.0
X_3 = np.fft.fftshift(np.fft.fft(x_3))

plt.subplot(3, 2, 1)
plt.stem(n, x_1)
plt.subplot(3, 2, 3)
plt.stem(w, np.abs(X_1))
plt.subplot(3, 2, 5)
plt.stem(w, np.angle(X_1))

plt.subplot(3, 2, 2)
plt.stem(n, xw_1)
plt.subplot(3, 2, 4)
plt.stem(w, np.abs(Xw_1))
plt.subplot(3, 2, 6)
plt.stem(w, np.angle(Xw_1))
plt.show()