import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wave

import CoupeBande as cb
import GetSound as sounds

samplingRate, dataBasson, dataGuitare = sounds.getSounds(False)

newDataBasson = cb.coupeBande(samplingRate, dataBasson, False)


wave.write("example.wav", samplingRate, newDataBasson.astype(np.int16))
