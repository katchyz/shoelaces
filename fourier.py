import numpy as np
import matplotlib.pyplot as plt
import cPickle as pickle
import gzip
import heapq

ribocov = np.array([5, 4, 3, 6, 4, 1, 5, 2, 0, 8, 3, 1, 6, 2, 0])
nts = np.array(range(0, len(ribocov)))

ft_ribocov = np.fft.fft(ribocov, axis=0)
amplitudes = abs(ft_ribocov)
frequencies = np.fft.fftfreq(len(ribocov), 1)
periods = 1 / frequencies

plt.figure()
plt.plot(periods, amplitudes, 'o')
plt.xlabel('Period (nt)')
plt.ylabel('Amplitude')
plt.xlim(0, len(data)+1)
plt.show()


################
################

### these are on offset data
### how to do this on raw ?
### overlap the whole CDS awyway ??

import cPickle as pickle
import gzip
import heapq

our = pickle.load(gzip.open('/Volumes/USELESS/META/OUR.p.gz', 'rb'))


for tr in our['Shield']:
	for i in range(0,7):
		ribocov = np.array(our['Shield'][tr][1].todense()[i])[0] # i=3: len28


cum_ribocov = np.array([])
for tr in our['Shield']:
	ribocov = np.array(our['Shield'][tr][1].todense()[3])[0] # 3: len28
	if not cum_ribocov.any(): # 1st round
		cum_ribocov = ribocov
		l = len(ribocov) # ??? only start ???
	elif len(ribocov) > len(cum_ribocov):
		cum_ribocov += ribocov[0:len(cum_ribocov)]
	else: # len(cum_ribocov) >= len(ribocov)
		cum_ribocov[0:len(ribocov)] += ribocov
		l = len(ribocov) # ??? only start ???


cum_ribocov = np.array([])
for tr in our['28hpf']:
	ribocov = np.array(our['28hpf'][tr][1].todense()[3])[0] # 3: len28
	if not cum_ribocov.any(): # 1st round
		cum_ribocov = ribocov
		l = len(ribocov) # ??? only start ???
	elif len(ribocov) > len(cum_ribocov):
		cum_ribocov += ribocov[0:len(cum_ribocov)]
	else: # len(cum_ribocov) >= len(ribocov)
		cum_ribocov[0:len(ribocov)] += ribocov
		l = len(ribocov) # ??? only start ???

ribocov = cum_ribocov[0:l] # ??? only start ??? # [offset:l] # offset=12
nts = np.array(range(0, len(ribocov))) # range(0, len(ribocov)-offset)

ft_ribocov = np.fft.fft(ribocov, axis=0)
amplitudes = abs(ft_ribocov)
frequencies = np.fft.fftfreq(len(ribocov), 1)
periods = 1 / frequencies

plt.figure('28hpf')
plt.plot(periods, amplitudes, 'o')
plt.xlabel('Period (nt)')
plt.ylabel('Amplitude')
plt.xlim(0, 15)
plt.show()

########

m1, m2, m3, m4, m5 = heapq.nlargest(5, amplitudes)
# idx is the first that is not inf or len(ribocov)
# idx = amplitudes.tolist().index(m3)
if amplitudes.tolist().index(m2) + amplitudes.tolist().index(m3) == len(ribocov): # if the period does not equal the whole interval
	idx = amplitudes.tolist().index(m4)
else:
	idx = amplitudes.tolist().index(m2)

################
### !!!!!!!!!!!!!!! or if in the x range of 0 to 15 the highest amplitude is at 3...
################
periods[idx]

if periods[idx] == 3.0:
	print 'Length XX shows periodicity!'
else:
	print 'Not periodic...'



################################
################################
################################

for stage in our:
	for fl in range(0,7):
		cum_ribocov = np.array([])
		for tr in our[stage]:
			ribocov = np.array(our[stage][tr][1].todense()[fl])[0] # 3: len28
			if not cum_ribocov.any(): # 1st round
				cum_ribocov = ribocov
				l = len(ribocov) # ??? only start ???
			elif len(ribocov) > len(cum_ribocov):
				cum_ribocov += ribocov[0:len(cum_ribocov)]
			else: # len(cum_ribocov) >= len(ribocov)
				cum_ribocov[0:len(ribocov)] += ribocov
				l = len(ribocov) # ??? only start ???
		ribocov = cum_ribocov[0:l] # ??? only start ??? # [offset:l] # offset=12
		nts = np.array(range(0, len(ribocov))) # range(0, len(ribocov)-offset)
		ft_ribocov = np.fft.fft(ribocov, axis=0)
		amplitudes = abs(ft_ribocov)
		frequencies = np.fft.fftfreq(len(ribocov), 1)
		periods = 1 / frequencies
		plt.figure(stage+str(fl+25))
		plt.plot(periods, amplitudes, 'o')
		plt.xlabel('Period (nt)')
		plt.ylabel('Amplitude')
		plt.xlim(0, 15)
		plt.show()



########
# Giraldez
gir = pickle.load(gzip.open('/Volumes/USELESS/META/Giraldez.p.gz', 'rb'))

for stage in gir:
	for fl in range(0,9):
		cum_ribocov = np.array([])
		for tr in gir[stage]:
			ribocov = np.array(gir[stage][tr][1].todense()[fl])[0] # 3: len28
			if not cum_ribocov.any(): # 1st round
				cum_ribocov = ribocov
				l = len(ribocov) # ??? only start ???
			elif len(ribocov) > len(cum_ribocov):
				cum_ribocov += ribocov[0:len(cum_ribocov)]
			else: # len(cum_ribocov) >= len(ribocov)
				cum_ribocov[0:len(ribocov)] += ribocov
				l = len(ribocov) # ??? only start ???
		ribocov = cum_ribocov[0:l] # ??? only start ??? # [offset:l] # offset=12
		nts = np.array(range(0, len(ribocov))) # range(0, len(ribocov)-offset)
		ft_ribocov = np.fft.fft(ribocov, axis=0)
		amplitudes = abs(ft_ribocov)
		frequencies = np.fft.fftfreq(len(ribocov), 1)
		periods = 1 / frequencies
		plt.figure(stage+' len'+str(fl+22))
		plt.plot(periods, amplitudes, 'o')
		plt.xlabel('Period (nt)')
		plt.ylabel('Amplitude')
		plt.xlim(0, 15)
		plt.show()


#######
#######
#######
#######
#######

# subplots ?
p = 0
for stage in our:
	print stage
	for fl in range(0,7):
		cum_ribocov = np.array([])
		for tr in our[stage]:
			ribocov = np.array(our[stage][tr][1].todense()[fl])[0] # 3: len28
			if not cum_ribocov.any(): # 1st round
				cum_ribocov = ribocov
				l = len(ribocov) # ??? only start ???
			elif len(ribocov) > len(cum_ribocov):
				cum_ribocov += ribocov[0:len(cum_ribocov)]
			else: # len(cum_ribocov) >= len(ribocov)
				cum_ribocov[0:len(ribocov)] += ribocov
				l = len(ribocov) # ??? only start ???
		ribocov = cum_ribocov[0:l] # ??? only start ??? # [offset:l] # offset=12
		nts = np.array(range(0, len(ribocov))) # range(0, len(ribocov)-offset)
		ft_ribocov = np.fft.fft(ribocov, axis=0)
		amplitudes = abs(ft_ribocov)
		frequencies = np.fft.fftfreq(len(ribocov), 1)
		periods = 1 / frequencies
		plt.figure('our')
		#plt.figure(stage+str(fl+25))
		plt.subplot(10,7,p+fl+1)
		plt.plot(periods, amplitudes * 1e-3)
		#plt.xlabel('Period (nt)'+stage+' len'+str(fl+25))
		#plt.ylabel('Amplitude')
		plt.xlim(0, 10)
	p += 7


plt.show()

###

gir = pickle.load(gzip.open('/Volumes/USELESS/META/Giraldez.p.gz', 'rb'))

p = 0
for stage in gir:
	print stage, '\n'
	for fl in range(0,9):
		cum_ribocov = np.array([])
		for tr in gir[stage]:
			ribocov = np.array(gir[stage][tr][1].todense()[fl])[0] # 3: len28
			if not cum_ribocov.any(): # 1st round
				cum_ribocov = ribocov
				l = len(ribocov) # ??? only start ???
			elif len(ribocov) > len(cum_ribocov):
				cum_ribocov += ribocov[0:len(cum_ribocov)]
			else: # len(cum_ribocov) >= len(ribocov)
				cum_ribocov[0:len(ribocov)] += ribocov
				l = len(ribocov) # ??? only start ???
		ribocov = cum_ribocov[0:l] # ??? only start ??? # [offset:l] # offset=12
		nts = np.array(range(0, len(ribocov))) # range(0, len(ribocov)-offset)
		ft_ribocov = np.fft.fft(ribocov, axis=0)
		amplitudes = abs(ft_ribocov)
		frequencies = np.fft.fftfreq(len(ribocov), 1)
		periods = 1 / frequencies
		plt.figure('Giraldez')
		plt.subplot(16,9,p+fl+1)
		plt.plot(periods, amplitudes * 1e-3)
		#plt.xlabel('Period (nt)')
		#plt.ylabel('Amplitude')
		plt.xlim(0, 10)
	p += 9

plt.show()


###

mouse = pickle.load(gzip.open('/Volumes/USELESS/META/mouse_none.p.gz', 'rb'))

p = 0
for stage in mouse:
	print stage, '\n'
	for fl in range(0,11):
		cum_ribocov = np.array([])
		for tr in mouse[stage]:
			ribocov = np.array(mouse[stage][tr][1].todense()[fl])[0] # 3: len28
			if not cum_ribocov.any(): # 1st round
				cum_ribocov = ribocov
				l = len(ribocov) # ??? only start ???
			elif len(ribocov) > len(cum_ribocov):
				cum_ribocov += ribocov[0:len(cum_ribocov)]
			else: # len(cum_ribocov) >= len(ribocov)
				cum_ribocov[0:len(ribocov)] += ribocov
				l = len(ribocov) # ??? only start ???
		ribocov = cum_ribocov[0:l] # ??? only start ??? # [offset:l] # offset=12
		nts = np.array(range(0, len(ribocov))) # range(0, len(ribocov)-offset)
		ft_ribocov = np.fft.fft(ribocov, axis=0)
		amplitudes = abs(ft_ribocov)
		frequencies = np.fft.fftfreq(len(ribocov), 1)
		periods = 1 / frequencies
		plt.figure('mouse_none')
		plt.subplot(3,4,p+fl+1)
		plt.plot(periods, amplitudes * 1e-3)
		#plt.xlabel('Period (nt)')
		#plt.ylabel('Amplitude')
		plt.xlim(0, 10)
	p += 11

plt.show()




######################
##### 3 column plots #
##### detect ORF #####

p = 0
plt.figure('our')
for stage in our:
	print stage
	for fl in range(0,7):
		cum_ribocov = np.array([])
		for tr in our[stage]:
			ribocov = np.array(our[stage][tr][1].todense()[fl])[0] # 3: len28
			if not cum_ribocov.any(): # 1st round
				cum_ribocov = ribocov
				l = len(ribocov) # ??? only start ???
			elif len(ribocov) > len(cum_ribocov):
				cum_ribocov += ribocov[0:len(cum_ribocov)]
			else: # len(cum_ribocov) >= len(ribocov)
				cum_ribocov[0:len(ribocov)] += ribocov
				l = len(ribocov) # ??? only start ???
		ribocov = cum_ribocov[0:l] # ??? only start ??? # [offset:l] # offset=12
		# add every 3rd
		orf = [0, 0, 0]
		for i in range(0, len(ribocov), 3):
			orf[0] += ribocov[i]
			orf[1] += ribocov[i+1]
			orf[2] += ribocov[i+2]
		plt.subplot(10,7,p+fl+1)
		plt.plot([1, 2, 3], orf)
	p += 7


plt.show()


##########
# concatenated (end to end, choose maybe dividable by 3)
# only ones with high coverage

our = pickle.load(gzip.open('/Volumes/USELESS/META/OUR.p.gz', 'rb'))

p = 0
plt.figure('our')
for stage in our:
	print stage
	for fl in range(0,7):
		cum_ribocov = np.array([])
		for tr in our[stage]:
			ribocov = np.array(our[stage][tr][1].todense()[fl])[0] # 3: len28
			# coverage threshold
			if (len(ribocov) % 3 == 0):
				cum_ribocov = np.append(cum_ribocov, ribocov)
		ft_ribocov = np.fft.fft(cum_ribocov, axis=0)
		amplitudes = abs(ft_ribocov)
		frequencies = np.fft.fftfreq(len(cum_ribocov), 1)
		periods = 1 / frequencies
		#plt.figure(stage+str(fl+25))
		plt.subplot(10,7,p+fl+1)
		plt.plot(periods, amplitudes * 1e-3)
		#plt.xlabel('Period (nt)'+stage+' len'+str(fl+25))
		#plt.ylabel('Amplitude')
		plt.xlim(0, 10)
	p += 7


plt.show()



############
# OTPG

p = 0
plt.figure('our')
for stage in our:
	print stage
	for fl in range(0,7):
		cum_ribocov = np.array([])
		for tr in otpg:
			if tr in our[stage]:
				ribocov = np.array(our[stage][tr][1].todense()[fl])[0] # 3: len28
				if not cum_ribocov.any(): # 1st round
					cum_ribocov = ribocov
					l = len(ribocov) # ??? only start ???
				elif len(ribocov) > len(cum_ribocov):
					cum_ribocov += ribocov[0:len(cum_ribocov)]
				else: # len(cum_ribocov) >= len(ribocov)
					cum_ribocov[0:len(ribocov)] += ribocov
					l = len(ribocov) # ??? only start ???
		ribocov = cum_ribocov[0:l] # ??? only start ??? # [offset:l] # offset=12
		nts = np.array(range(0, len(ribocov))) # range(0, len(ribocov)-offset)
		ft_ribocov = np.fft.fft(ribocov, axis=0)
		amplitudes = abs(ft_ribocov)
		frequencies = np.fft.fftfreq(len(ribocov), 1)
		periods = 1 / frequencies
		plt.subplot(10,7,p+fl+1)
		plt.plot(periods, amplitudes * 1e-3)
		plt.xlim(0, 10)
	p += 7


plt.show()


#####
gir = pickle.load(gzip.open('/Volumes/USELESS/META/Giraldez.p.gz', 'rb'))

p = 0
plt.figure('gir')
for stage in gir:
	print stage
	for fl in range(0,9):
		cum_ribocov = np.array([])
		for tr in otpg:
			if tr in gir[stage]:
				ribocov = np.array(gir[stage][tr][1].todense()[fl])[0] # 3: len28
				if not cum_ribocov.any(): # 1st round
					cum_ribocov = ribocov
					l = len(ribocov) # ??? only start ???
				elif len(ribocov) > len(cum_ribocov):
					cum_ribocov = np.append(cum_ribocov, np.zeros(len(ribocov)-len(cum_ribocov)))
					cum_ribocov += ribocov
				else: # len(cum_ribocov) >= len(ribocov)
					cum_ribocov[0:len(ribocov)] += ribocov
					l = len(ribocov) # ??? only start ???
		ribocov = cum_ribocov[0:500] # ??? only start ??? # [offset:l] # offset=12 ### GET FIRST 500 NT ###
		nts = np.array(range(0, len(ribocov))) # range(0, len(ribocov)-offset)
		ft_ribocov = np.fft.fft(ribocov, axis=0)
		amplitudes = abs(ft_ribocov)
		frequencies = np.fft.fftfreq(len(ribocov), 1)
		periods = 1 / frequencies
		plt.subplot(16,9,p+fl+1)
		plt.plot(periods, amplitudes * 1e-3)
		plt.xlim(0, 10)
	p += 9


plt.show()

##########
##########
##########
##########

p = 0
plt.figure('our')
for stage in our:
	print stage
	for fl in range(0,7):
		cum_ribocov = np.array([])
		for tr in otpg:
			if tr in our[stage]:
				ribocov = np.array(our[stage][tr][1].todense()[fl])[0] # 3: len28
				if not cum_ribocov.any(): # 1st round
					cum_ribocov = ribocov
					l = len(ribocov) # ??? only start ???
				elif len(ribocov) > len(cum_ribocov):
					cum_ribocov = np.append(cum_ribocov, np.zeros(len(ribocov)-len(cum_ribocov)))
					cum_ribocov += ribocov
				else: # len(cum_ribocov) >= len(ribocov)
					cum_ribocov[0:len(ribocov)] += ribocov
					l = len(ribocov) # ??? only start ???
		ribocov = cum_ribocov[0:500] # ??? only start ??? # [offset:l] # offset=12 ### GET FIRST 500 NT ### if we have such long CDSs
		nts = np.array(range(0, len(ribocov))) # range(0, len(ribocov)-offset)
		ft_ribocov = np.fft.fft(ribocov, axis=0)
		amplitudes = abs(ft_ribocov)
		frequencies = np.fft.fftfreq(len(ribocov), 1)
		periods = 1 / frequencies
		plt.subplot(10,7,p+fl+1)
		plt.plot(periods, amplitudes * 1e-3)
		plt.xlim(0, 10)
	p += 7


plt.show()



################
################
# fruitfly

ff = pickle.load(gzip.open('/Volumes/USELESS/META/fruitfly_meta/fruitfly.p.gz', 'rb'))

p = 0
plt.figure('fruitfly')
for stage in ff:
	print stage, '\n'
	no_lengths = len(ff[stage]['FBtr0089573'][0].todense())
	for fl in range(0,no_lengths):
		cum_ribocov = np.array([])
		for tr in ff[stage]:
			if tr in ff[stage]:
				ribocov = np.array(ff[stage][tr][1].todense()[fl])[0] # 3: len28
				if not cum_ribocov.any(): # 1st round
					cum_ribocov = ribocov
					l = len(ribocov) # ??? only start ???
				elif len(ribocov) > len(cum_ribocov):
					cum_ribocov = np.append(cum_ribocov, np.zeros(len(ribocov)-len(cum_ribocov)))
					cum_ribocov += ribocov
				else: # len(cum_ribocov) >= len(ribocov)
					cum_ribocov[0:len(ribocov)] += ribocov
					l = len(ribocov) # ??? only start ???
		ribocov = cum_ribocov[0:500] # ??? only start ??? # [offset:l] # offset=12 ### GET FIRST 500 NT ### if we have such long CDSs
		# nts = np.array(range(0, len(ribocov))) # range(0, len(ribocov)-offset)
		ft_ribocov = np.fft.fft(ribocov, axis=0)
		amplitudes = abs(ft_ribocov)
		frequencies = np.fft.fftfreq(len(ribocov), 1)
		periods = 1 / frequencies
		plt.subplot(10,11,p+fl+1)
		plt.plot(periods, amplitudes * 1e-3)
		plt.xlim(0, 10)
	p += 11


plt.show()
