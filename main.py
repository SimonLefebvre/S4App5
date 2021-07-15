import numpy as np
from scipy.io import wavfile as wave
import matplotlib.pyplot as plt
import addcopyfighandler

import CoupeBande as cb
import GetSound as sounds
import GetPeaks as peaks
import GenerateSound as gen
import PasserParEnBas as env

plot = True

plt.rcParams['savefig.format'] = 'svg'

samplingRate, dataBasson, dataGuitare = sounds.getSounds(True)

newDataBasson = cb.coupeBande(dataBasson, samplingRate, True)

amplitudePeak, anglePeak = peaks.getPeaks(dataGuitare, samplingRate, 465, False)
gSOL = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(dataGuitare), 392, False)
gMIb = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(dataGuitare), 311.1, False)
gFA = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(dataGuitare), 349.2, False)
gRE = gen.changeNote(amplitudePeak, anglePeak, samplingRate, len(dataGuitare), 293.7, False)

amplitudePeak, anglePeak = peaks.getPeaks(newDataBasson, samplingRate, 200, False)
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

silence = np.zeros(10000)

gMusic = np.append(gNote1[7000:30000], gNote1[7000:30000])
gMusic = np.append(gMusic, gNote1[7000:30000])
gMusic = np.append(gMusic, gNote2[7000::])
gMusic = np.append(gMusic, silence)

gMusic = np.append(gMusic, gNote3[7000:30000])
gMusic = np.append(gMusic, gNote3[7000:30000])
gMusic = np.append(gMusic, gNote3[7000:30000])
gMusic = np.append(gMusic, gNote4[7000::])

bMusic = np.append(bNote1[22500:70000], bNote1[24000:70000])
bMusic = np.append(bMusic, bNote1[24000:70000])
bMusic = np.append(bMusic, bNote2[24000::])
bMusic = np.append(bMusic, silence)

bMusic = np.append(bMusic, bNote3[22500:70000])
bMusic = np.append(bMusic, bNote3[24000:70000])
bMusic = np.append(bMusic, bNote3[24000:70000])
bMusic = np.append(bMusic, bNote4[24000::])

#plt.figure()
#plt.plot(np.fft.fftfreq(len(gNote1), 1/ samplingRate), 20*np.log10((np.abs(np.fft.fft(gNote1)))))
plt.tight_layout()
plt.show()

wave.write("MusicGuitare.wav", samplingRate, gMusic.astype(np.int16))
wave.write("MusicBasson.wav", samplingRate, bMusic.astype(np.int16))
