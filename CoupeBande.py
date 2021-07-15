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

    N = 1024  # Ordre du filtre coupe bande
    w0 = 2 * f0 * np.pi / fs  # Fréquence a filtrer normalisé de 0 a 2pi

    n = np.arange(-N / 2, N / 2, 1)
    K = 1  # np.round(2 * (fc / fs * N) + 1) + 1
    print(K)

    # Filtre passe bas à fréquence de coupure à 20 Hz
    h_low = (1 / N) * np.sin(np.pi * n * K / N) / (np.sin(np.pi * n / N) + 1e-20)
    h_low[int(N / 2)] = K / N

    # Création du dirac
    dirac = np.zeros(N)
    dirac[int(N / 2)] = 1.0

    # Réponse impulsionelle du filtre passe bas transformé en coupe bande
    h = dirac - 2 * h_low * np.cos(w0 * n)

    N1 = x.shape[0]
    N2 = h.shape[0]
    N3 = N1 + N2 - 1  # New M length

    X = np.fft.fft(x, N3)  # FFT to get X in frequential
    H = np.fft.fft(h, N3)  # FFT to get H in frequential

    # Multiple filter PASS to get the filter to work even better
    Y = X * H
    Y = Y * H
    Y = Y * H

    y = np.real(np.fft.ifft(Y, N3))  # Reverse FFT to get the output in time of M length

    if (plot == True):
        plt.figure()
        plt.subplot(3, 2, 1)
        plt.semilogy()
        plt.plot(np.fft.fftfreq(len(X), 1 / fs), np.abs(X))
        plt.title('fft avant filtre')

        plt.subplot(3, 2, 3)
        plt.plot(np.fft.fftfreq(len(H), 1 / fs), 20 * np.log10(np.abs(H)))
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

        # m = np.arange(0, len(y) / fs, 1 / fs)
        # plt.subplot(3, 2, 6)
        # plt.plot(m, y)
        # plt.title('data apres filtre')

        t = np.arange(0, len(x) / fs, 1 / fs)
        sin = np.sin(2 * np.pi * 1000 * t)
        plt.figure('réponse sin 1000Hz')
        plt.subplot(2, 1, 1)
        plt.plot(t, sin)
        plt.xlabel('Temps (s)')
        plt.ylabel('Amplitude')
        plt.title('Signal entrée')

        plt.subplot(2, 1, 2)
        rep = np.convolve(h, sin)
        plt.plot(np.arange(0, len(rep) / fs, 1 / fs), rep)
        plt.xlabel('Temps (s)')
        plt.ylabel('Amplitude')
        plt.title('Signal sortie')
        plt.tight_layout()

        plt.figure('avant vs apres')
        plt.subplot(2, 1, 1)
        plt.plot(np.fft.fftfreq(len(X), 1 / fs), 20 * np.log10(np.abs(X)))
        plt.title('signal entrée')

        plt.subplot(2, 1, 2)
        plt.plot(np.fft.fftfreq(len(Y), 1 / fs), 20 * np.log10(np.abs(Y)))
        plt.title('signal Sortie')

        plt.tight_layout()

    return y
