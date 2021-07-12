import CoupeBande as cb
import GetSound as sounds
import GetPeaks as peaks
import GenerateSound as gen

samplingRate, dataBasson, dataGuitare = sounds.getSounds(False)

newDataBasson = cb.coupeBande(samplingRate, dataBasson, False)

amplitudePeak, anglePeak, frequencyPeak = peaks.getPeaks(dataGuitare, samplingRate, 465)
gen.generateSound(amplitudePeak, anglePeak, frequencyPeak, samplingRate, len(dataGuitare), 'MyGuitare.wav')

amplitudePeak, anglePeak, frequencyPeak = peaks.getPeaks(newDataBasson, samplingRate, 465)
gen.generateSound(amplitudePeak, anglePeak, frequencyPeak, samplingRate, len(dataGuitare), 'MyBasson.wav')
