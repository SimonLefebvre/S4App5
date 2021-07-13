import matplotlib.pyplot as plt
import numpy as np


# data: raw .wave data
# samplingRate: of the .wav data in Hz
# plot : true to plot figures of the envelop
# generatedData: The syntetisation of the sound
#
# returns the generated data changed by the envelop of the .wav file
def envelop(x, samplingRate, plot, generatedData):

    K = 885
    a = 1 / K
    start = 0
    stop = np.pi * 2
    step = stop / len(x)

    w = np.arange(start, stop, step)
    t = np.arange(0, len(x) / samplingRate, 1 / samplingRate)

    X = np.fft.fft(np.abs(x))

    H = (a * np.sin(K * w / 2)) / (np.sin(w / 2) + 1e-20)
    H[0] = a * K

    Y = H * X
    y = np.real(np.fft.ifft(Y))

    Sortie = generatedData * y
    Sortie = Sortie / 150000000

    if (plot == True):
        plt.figure('Envelop')

        plt.subplot(3, 2, 1)
        plt.ylabel('x')
        plt.xlabel('temps (s)')
        plt.plot(t, x)

        plt.subplot(3, 2, 3)
        plt.ylabel('y')
        plt.xlabel('temps (s)')
        plt.plot(t, y)

        plt.subplot(3, 2, 5)
        plt.ylabel('Note avec enveloppe')
        plt.xlabel('temps (s)')
        plt.plot(t, Sortie)

        plt.subplot(3, 2, 2)
        plt.ylabel('X')
        plt.xlabel('Fréquence (Hz)')
        plt.plot(np.fft.fftfreq(len(X), 1 / samplingRate), np.abs(X))

        plt.subplot(3, 2, 4)
        plt.ylabel('H')
        plt.xlabel('Fréquence (Hz)')
        plt.plot(np.fft.fftfreq(len(H), 1 / samplingRate), np.abs(H))

        plt.subplot(3, 2, 6)
        plt.ylabel('Y')
        plt.xlabel('Fréquence (Hz)')
        plt.plot(np.fft.fftfreq(len(Y), 1 / samplingRate), np.abs(Y))

    return Sortie
