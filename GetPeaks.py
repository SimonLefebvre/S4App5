from scipy.signal import find_peaks
import numpy as np


def getPeaks(dataGuitare, fs):
    y_guitar = np.fft.fft(dataGuitare)
    foundPeaks, property = find_peaks(np.abs(y_guitar), distance=(465 * 160000 / (fs)))

    indexPeak = np.zeros(32)
    amplitudePeak = np.zeros(32)
    frequencyPeak = np.zeros(32)
    anglePeak = np.zeros(32)

    for i in range(0, 32):
        indexPeak[i] = foundPeaks[i]
        amplitudePeak[i] = np.abs(y_guitar[int(indexPeak[i])])
        anglePeak[i] = np.angle(y_guitar[int(indexPeak[i])])
        frequencyPeak[i] = indexPeak[i] * fs / 160000

    return indexPeak, amplitudePeak, anglePeak, frequencyPeak
