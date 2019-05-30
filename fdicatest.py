import numpy as np
import sys
import scipy.io.wavfile as wf
from FDICA import FDICA,ICA
from sound_mixing import Preprocessing

#prepare data
rate1, data1 = wf.read('./samples/raw_1.wav')
rate2, data2 = wf.read('./samples/raw_2.wav')
rate3, data3 = wf.read('./samples/raw_3.wav')
if rate1 != rate2 or rate2 != rate3:
    raise ValueError('Sampling_rate_Error')


data1 = data1.T[0,400000:800000]
data2 = data2.T[0,400000:800000]
data3 = data3.T[0,400000:800000]

data = np.vstack([data1.astype(float), data2.astype(float), data3.astype(float)])

x = Preprocessing(data,10).mixing()


y = FDICA(x, sample_freq=rate1).fdica()

y = [(y_i * 32767 / max(np.absolute(y_i))).astype(np.int16) for y_i in np.asarray(y)]

wf.write('./samples/fdica_1_out.wav', rate1, y[0])
wf.write('./samples/fdica_2_out.wav', rate2, y[1])
wf.write('./samples/fdica_3_out.wav', rate3, y[2])