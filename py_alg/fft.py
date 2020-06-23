import numpy as np
import matplotlib.pyplot as plt

cds1 = np.array([18, 6, 2, 29, 11, 0, 10, 5, 3, 17, 9, 4])
cds2 = np.array([12, 4, 1, 9, 2, 0])
cds3 = np.array([14, 10, 7, 12, 4, 3, 19, 5, 2, 20, 11, 3, 13, 4, 2])

CDSs = [cds1, cds2, cds3]

cumRibocov = np.array([])
for cds in CDSs:
	if not cumRibocov.any(): # 1st
		cumRibocov = cds
	elif len(cds) > len(cumRibocov):
		cumRibocov = np.append(cumRibocov, np.zeros(len(cds)-len(cumRibocov)))
		cumRibocov += cds
	else: # len(cumRibocov) >= len(cds)
		cumRibocov[0:len(cds)] += cds


l = 9
riboCov = cumRibocov[0:l]
ft = np.fft.fft(riboCov, axis=0)
amplitudes = abs(ft)
frequencies = np.fft.fftfreq(len(riboCov), 1)
periods = 1/frequencies

plt.plot(periods, amplitudes) # plt.plot(abs(periods), amplitudes)
plt.xlim(0,10)
plt.show()


#########
for i in range(1, len(periods)/2+1):
	if periods[i] < 10:
		idxStart = i
		break


maxAmpIdx = np.argmax(amplitudes[idxStart:len(periods)/2+1]) + 1
if periods[maxAmpIdx] == 3.0:
	print 'periodic!'

