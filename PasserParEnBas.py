import matplotlib.pyplot as plt
import numpy as np


# data: raw .wave data
# samplingRate: of the .wav data in Hz
# plot : true to plot figures of the envelop
# generatedData: The syntetisation of the sound
#
# returns the generated data changed by the envelop of the .wav file
def envelop(data, samplingRate, plot, generatedData):
    dataFreq = np.fft.fft(np.abs(data))
    xvalues = np.fft.fftfreq(len(dataFreq), (1.0 / samplingRate))

    K = 885
    a = 1 / K
    start = 0
    stop = np.pi * 2
    step = stop / len(dataFreq)

    w = np.arange(start, stop, step)

    H_m = (a * np.sin(K * w / 2)) / (np.sin(w / 2) + 1e-20)
    H_m[0] = a * K
    Enveloppe_FREQ = H_m * dataFreq;
    if (plot == True):
        plt.figure()
        plt.subplot(3, 1, 1)
        plt.stem(w, H_m)
        plt.subplot(3, 1, 2)
        plt.plot(xvalues, np.abs(dataFreq))

        plt.subplot(3, 1, 3)
        plt.plot(xvalues, np.abs(Enveloppe_FREQ))
        plt.show()

    Enveloppe_TEMP = np.abs(np.real( np.fft.ifft(Enveloppe_FREQ)))

    if (plot == True):
        plt.figure()
        plt.plot(Enveloppe_TEMP)
        plt.show()

    GeneratedDataFREQ = np.fft.fft(generatedData)

    Sortie_FREQ = GeneratedDataFREQ * Enveloppe_FREQ
    #Sortie = np.real(np.fft.ifft(Sortie_FREQ))
    Sortie = generatedData * Enveloppe_TEMP
    Sortie = Sortie / 150000000

    if (plot == True):
        plt.figure()
        plt.subplot(3, 1, 1)
        plt.plot(np.abs(GeneratedDataFREQ))
        plt.subplot(3, 1, 2)
        plt.plot(np.abs(Sortie_FREQ))
        plt.subplot(3, 1, 3)
        plt.plot(Sortie)
        plt.show()
        
        
    return Sortie
