import matplotlib.pyplot as plt
import numpy as np


# ENTRÉES
# Ce filtre coupe-bande filtre à 1000 Hz d'un largeur de 20 Hz
# x  -> Data en temporelle à filtrer
# fs -> Fréquence d'échantillonage
# RETURNS
# Même signal que obtenue en entrée sans les 1000 Hz et de longueur différente

def coupeBande(x, fs, plot):
    fc = 20  # Largeur de fréquence du coupe bande (w1) mais en Hz
    f0 = 1000  # Fréquence à filtrer (w0) mais en Hz

    N = 1025  # Ordre du filtre coupe bande
    w0 = 2 * f0 * np.pi / fs  # Fréquence a filtrer normalisé de -pi a pi

    n = np.arange(-N / 2, N / 2, 1) # axe des x temporelle discret non normalisé
    K = 2 * (fc / fs * N) + 2

    # Filtre passe bas à fréquence de coupure à 1000 Hz
    h_low = (1 / N) * np.sin(np.pi * n * K / N) / (np.sin(np.pi * n / N) + 1e-20)
    h_low[int(N / 2)] = K / N

    # Création du dirac
    dirac = np.zeros(N)
    dirac[int(N / 2)] = 1.0

    # Réponse impulsionelle du filtre passe bas transformé en coupe bande
    h = dirac - 2 * h_low * np.cos(w0 * n)

    N1 = x.shape[0]
    N2 = h.shape[0]
    N3 = N1 + N2 - 1 #New M length

    X = np.fft.fft(x, N3) #FFT to get X in frequential
    H = np.fft.fft(h, N3) #FFT to get H in frequential

    # Multiple filter PASS to get the filter to work even better
    Y = X * H
    Y = Y * H
    Y = Y * H

    y = np.real(np.fft.ifft(Y, N3)) # Reverse FFT to get the output in time of M length

    if (plot == True):
        plt.figure()
        plt.subplot(3, 2, 1)
        plt.semilogy()
        plt.plot(np.fft.fftfreq(len(X), 1 / fs), np.abs(X))
        plt.title('fft avant filtre')

        plt.subplot(3, 2, 3)
        plt.plot(np.fft.fftfreq(len(H), 1 / fs), np.abs(H))
        plt.title('filtre')

        plt.subplot(3, 2, 5)
        plt.semilogy()
        plt.plot(np.fft.fftfreq(len(Y), 1 / fs), np.abs(Y))
        plt.title('fft apres filtre')

        m = np.arange(0, len(x) / fs, 1 / fs)

        plt.subplot(3, 2, 2)
        plt.plot(m, x)
        plt.title('data avant filtre')

        plt.subplot(3, 2, 4)
        plt.plot(h)
        plt.title('filtre')

        m = np.arange(0, len(y) / fs, 1 / fs)
        plt.subplot(3, 2, 6)
        plt.plot(m, y)
        plt.title('data apres filtre')

        plt.show()

    return y
