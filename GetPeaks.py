from scipy.signal import find_peaks
import numpy as np


# Entrées
# Data -> raw data in time
# fs -> Fréquence de coupure
# fFund -> Fréquence de la fondamentale

# RETURNS
# amplitudePeak -> Tableau des 32 peak trouvé
# anglePeak     -> Tableau des 32 phases
def getPeaks(data, fs, fFund, showFrequency):
    fft = np.fft.fft(data)
    foundPeaks, property = find_peaks(np.abs(fft), distance=(fFund * len(data) / fs))

    amplitudePeak = np.zeros(32)
    frequencyPeak = np.zeros(32)
    anglePeak = np.zeros(32)

    offset = 0
    if foundPeaks[0] < fFund * len(data) / fs:
        offset = 1

    for i in range(0, 32):
        amplitudePeak[i] = np.abs(fft[foundPeaks[i + offset]])
        anglePeak[i] = np.angle(fft[foundPeaks[i + offset]])
        frequencyPeak[i] = foundPeaks[i + offset] * fs / len(data)

    if showFrequency == True:
        print(frequencyPeak)

    return amplitudePeak, anglePeak
