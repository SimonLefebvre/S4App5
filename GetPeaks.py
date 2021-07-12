from scipy.signal import find_peaks
import numpy as np

import matplotlib.pyplot as plt
from scipy.io import wavfile as wave


def getPeaks(dataGuitare, fs, plot):
    y_guitar = np.fft.fft(dataGuitare)
    x_guitar = np.fft.fftfreq(len(y_guitar), (1.0 / fs))

    foundPeaks, property = find_peaks(np.abs(y_guitar), distance=(465 * 160000 / (fs)))
    print(foundPeaks[0]*fs/160000)

    n = np.arange(0, 160000)
    n = n * (1/fs)
    rep = np.abs(y_guitar[foundPeaks[0]]) * np.sin((2*np.pi*(foundPeaks[0]*fs/160000) * n) + np.angle(y_guitar[foundPeaks[0]]))
    print(np.abs(y_guitar[foundPeaks[0]]))
    print(np.abs(y_guitar[foundPeaks[0]]))

    for i in range(1, 31):
        rep = rep + np.abs(y_guitar[foundPeaks[i]]) * np.sin((2*np.pi*(foundPeaks[i]*fs/160000) * n) + np.angle(y_guitar[foundPeaks[i]]))
        print(np.abs(y_guitar[foundPeaks[i]]))
        print(foundPeaks[i]*fs/160000)
    rep = rep/10000
    plt.figure()
    plt.plot(rep)

    plt.show()
    wave.write("MaGuitare.wav", fs, rep.astype(np.int16))

    return foundPeaks
