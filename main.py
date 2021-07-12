import CoupeBande as cb
import GetSound as sounds
import GetPeaks as peaks
import GenerateSound as gen

samplingRate, dataBasson, dataGuitare = sounds.getSounds(False)

newDataBasson = cb.coupeBande(samplingRate, dataBasson, False)

indexPeak, amplitudePeak, anglePeak, frequencyPeak = peaks.getPeaks(dataGuitare, samplingRate)
gen.generateSound(indexPeak, amplitudePeak, anglePeak, frequencyPeak, samplingRate, len(dataGuitare))
