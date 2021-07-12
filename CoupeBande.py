import matplotlib.pyplot as plt
import numpy as np


def coupeBande(fs, data, plot):
    fc = 20
    f0 = 1000

    N = 1024
    w0 = f0 * np.pi / 22050

    n = np.arange(-N / 2, N / 2)
    K = 2 * (fc / fs * N) + 1

    h = (1 / N) * np.sin(np.pi * n * K / N) / (np.sin(np.pi * n / N) + 1e-20)
    h[int(N / 2)] = K / N

    dirac = np.zeros(N)
    dirac[int(N / 2)] = 1.0

    coupeBande = dirac - 2 * h * np.cos(w0 * n)
    H_coupe = np.fft.fft(coupeBande)

    rep = np.convolve(coupeBande, data)
    rep = np.convolve(coupeBande, rep)
    rep = np.convolve(coupeBande, rep)
    rep = np.convolve(coupeBande, rep)
    rep = np.convolve(coupeBande, rep)
    rep = np.convolve(coupeBande, rep)

    if (plot == True):
        plt.figure()
        plt.title('Filtre coupe bande')
        plt.plot(np.fft.fftfreq(len(H_coupe), (1/fs)), np.abs(H_coupe))
        plt.show()

    return rep
