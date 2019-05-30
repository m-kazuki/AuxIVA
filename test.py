import numpy as np
import sys
import scipy.io.wavfile as wf
from fastAuxIVA import AuxIVA
from sound_mixing import Preprocessing

#prepare data
rate0, data0 = wf.read('./samples/samples/group/output.wav')

data0 = data0.astype(float).T


y = AuxIVA(data0, sample_freq=rate0,beta=0.3).auxiva()

y = [(y_i * 32767 / max(np.absolute(y_i))).astype(np.int16) for y_i in np.asarray(y)]

wf.write('./samples/samples/group/auxiva_0.wav', rate0, y[0])
wf.write('./samples/samples/group/auxiva_1.wav', rate0, y[1])
wf.write('./samples/samples/group/auxiva_2.wav', rate0, y[2])
