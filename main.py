import numpy as np
from scipy.io import wavfile as wave
import matplotlib.pyplot as plt

import CoupeBande as cb
import GetSound as sounds
import GetPeaks as peaks
import GenerateSound as gen
import PasserParEnBas as env

plot = True

samplingRate, dataBasson, dataGuitare = sounds.getSounds(False)

newDataBasson = cb.coupeBande(dataBasson, samplingRate, True)

amplitudePeak, anglePeak = peaks.getPeaks(dataGuitare, samplingRate, 465, True)
gSOL = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(dataGuitare), 392, False)
gMIb = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(dataGuitare), 311.1, False)
gFA = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(dataGuitare), 349.2, False)
gRE = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(dataGuitare), 293.7, False)

amplitudePeak, anglePeak = peaks.getPeaks(newDataBasson, samplingRate, 200, True)
bSOL = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(newDataBasson), 392/2, False)
bMIb = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(newDataBasson), 311.1/2, False)
bFA = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(newDataBasson), 349.2/2, False)
bRE = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(newDataBasson), 293.7/2, False)

bNote1 = env.envelop(newDataBasson, samplingRate, False, bSOL)
bNote2 = env.envelop(newDataBasson, samplingRate, False, bMIb)
bNote3 = env.envelop(newDataBasson, samplingRate, False, bFA)
bNote4 = env.envelop(newDataBasson, samplingRate, False, bRE)

gNote1 = env.envelop(dataGuitare, samplingRate, False, gSOL)
gNote2 = env.envelop(dataGuitare, samplingRate, False, gMIb)
gNote3 = env.envelop(dataGuitare, samplingRate, False, gFA)
gNote4 = env.envelop(dataGuitare, samplingRate, False, gRE)

gMusic = np.append(gNote1[7000:30000], gNote1[7000:30000])
gMusic = np.append(gMusic, gNote1[7000:30000])
gMusic = np.append(gMusic, gNote2[7000::])

gMusic = np.append(gMusic, gNote3[7000:30000])
gMusic = np.append(gMusic, gNote3[7000:30000])
gMusic = np.append(gMusic, gNote3[7000:30000])
gMusic = np.append(gMusic, gNote4[7000::])

bMusic = np.append(bNote1[22500:55000], bNote1[22500:55000])
bMusic = np.append(bMusic, bNote1[22500:55000])
bMusic = np.append(bMusic, bNote2[22500::])

bMusic = np.append(bMusic, bNote3[22500:55000])
bMusic = np.append(bMusic, bNote3[22500:55000])
bMusic = np.append(bMusic, bNote3[22500:55000])
bMusic = np.append(bMusic, bNote4[22500::])

plt.figure()
plt.plot(bMusic)
plt.show()

wave.write("MusicGuitare.wav", samplingRate, gMusic.astype(np.int16))
wave.write("MusicBasson.wav", samplingRate, bMusic.astype(np.int16))
