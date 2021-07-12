import numpy as np
from scipy.io import wavfile as wave

def generateSound(indexPeak, amplitudePeak, anglePeak, frequencyPeak, fs, len):
    n = np.arange(0, 160000)
    n = n * (1 / fs)
    rep = amplitudePeak[0] * np.sin((2 * np.pi * frequencyPeak[0] * n) + anglePeak[0])

    for i in range(1, 31):
        rep = rep + amplitudePeak[i] * np.sin((2 * np.pi * frequencyPeak[i] * n) + anglePeak[i])

    wave.write("MaGuitare.wav", fs, rep.astype(np.int16))