import numpy as np
import matplotlib.pyplot as plt

def changeNote(amplitudePeak, anglePeak, fs, len, newFrequency, plot):
    n = np.arange(0, len)
    n = n * (1 / fs)
    rep = amplitudePeak[0] * np.sin((2 * np.pi * newFrequency * n) - anglePeak[0])

    for i in range(1, 32):
        rep = rep + amplitudePeak[i] * np.sin((2 * np.pi * (newFrequency * (i + 1)) * n) - anglePeak[i])

    if plot == True:
        plt.figure()
        plt.plot(rep)
        plt.show()

    return rep