import numpy as np
import matplotlib.pyplot as plt

N = np.arange(2, 1024)

fs = 44100
fc = fs/1000
n = N*fc/fs
K = (n*2)+1

Eq1 = ((1 / N) * (np.sin((np.pi * n * K) / N) / np.sin((np.pi * n) / N)))
y = np.zeros(44200)
for i in range(0, len(y)):
    y[i] = 0.707
plt.stem(N, Eq1)
plt.show()

print('N')
print(N)
print('n')
print(n)
print('K')
print(K)