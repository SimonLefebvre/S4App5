import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile as wave

import CoupeBande as cb
import GetSound as sounds
import GetPeaks as peaks

samplingRate, dataBasson, dataGuitare = sounds.getSounds(False)

newDataBasson = cb.coupeBande(samplingRate, dataBasson, False)

p = peaks.getPeaks(dataGuitare, samplingRate, True)



