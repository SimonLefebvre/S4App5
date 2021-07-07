import matplotlib.pyplot as plt
import numpy as np

N= 32
fc = 2000
fs = 16000
M = 256

K = 2*(fc/fs*N)+1

n = np.arange(-N/2, N/2)
m = np.arange(-M/2, M/2)
w = 2*np.pi*m/M

h = (1/N) * np.sin(np.pi*n*K/N) / (np.sin(np.pi*n/N)+1e-20)
h[int(N/2)] = K/N
win = np.hanning(N)
hw = h * win

H = np.fft.fftshift(np.fft.fft(h, M))
Hw = np.fft.fftshift(np.fft.fft(hw, M))

N2 = 128
n2 = np.arange(0, N2)
A1 = 1
A2 = 0.25
f1 = 200
f2 = 3000

x1 = A1*np.sin(2*np.pi*f1*n2/fs)
x2 = A2*np.sin(2*np.pi*f2*n2/fs)
x = x1+x2

y = np.convolve(h, x)
yw = np.convolve(hw, x)

N3 = h.shape[0]
N4 = x.shape[0]
N5 = N3+N4-1

H1 = np.fft.fft(h, N5)
X1 = np.fft.fft(x, N5)
Y = H1*X1
y2 = np.real(np.fft.ifft(Y, N5))
plt.subplot(4, 1, 4)
plt.plot(y2)



print(h)
plt.subplot(4, 1, 1)
plt.plot(x)
plt.subplot(4, 1, 2)
plt.plot(y)
plt.subplot(4, 1, 3)
plt.plot(yw)
plt.show()