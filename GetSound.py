import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wave


def getSounds(plot):
    samplingRate, dataBasson = wave.read('AudioFiles/note_basson_plus_sinus_1000_Hz.wav')
    y_basson = np.fft.fft(dataBasson)
    x_basson = np.fft.fftfreq(len(y_basson), (1.0 / samplingRate))

    samplingRate, dataGuitare = wave.read('AudioFiles/note_guitare_LAd.wav')
    y_guitar = np.fft.fft(dataGuitare)
    x_guitar = np.fft.fftfreq(len(y_guitar), (1.0 / samplingRate))

    if (plot == True):
        plt.figure('fft des deux instruments')

        plt.subplot(2, 1, 1)
        plt.title('fft La# Guitar')
        plt.xlabel('Fréquence (Hz)')
        plt.ylabel('Amplitude')
        plt.semilogy()
        plt.plot(x_guitar, np.abs(y_guitar))


        plt.subplot(2, 1, 2)
        plt.title('fft Basson')
        plt.xlabel('Fréquence (Hz)')
        plt.ylabel('Amplitude')
        plt.semilogy()
        plt.plot(x_basson, np.abs(y_basson))

    return samplingRate, dataBasson, dataGuitare
