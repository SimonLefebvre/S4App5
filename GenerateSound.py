import numpy as np
from scipy.io import wavfile as wave

def generateSound(amplitudePeak, anglePeak, frequencyPeak, fs, len, name):
    n = np.arange(0, len)
    n = n * (1 / fs)
    rep = amplitudePeak[0] * np.sin((2 * np.pi * frequencyPeak[0] * n) + anglePeak[0])

    for i in range(1, 31):
        rep = rep + amplitudePeak[i] * np.sin((2 * np.pi * frequencyPeak[i] * n) + anglePeak[i])

    rep = rep / 10000
    wave.write(name, fs, rep.astype(np.int16))