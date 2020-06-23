# https://pypi.python.org/pypi/changepoint/0.1.1

import numpy as np
from changepoint.mean_shift_model import MeanShiftModel

data = np.array([12, 14, 20, 31, 16, 17, 21, 174, 180, 131, 140, 113, 100, 106, 91])
model = MeanShiftModel()
stats, pvals, nums = model.detect_mean_shift(data)

#ind = np.argmax(stats)
# ind is the index of the value in data array where change happens
# (from 21 to 154)


#########################################
### ...use the vector positions from -15 to -5

changes = np.zeros(len(stats)-1)
for s in range(len(stats)-1):
	changes[s] = stats[s+1] -  stats[s]


ind = np.argmax(abs(changes))+1
# ind is the index of the value in data array where change happens