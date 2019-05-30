import numpy as np
import sys
import cis
import scipy.io.wavfile as wf
from IVA import IVA
from sound_mixing import Preprocessing

#prepare data
rate1, data1 = cis.wavread('./samples/music1.wav')
rate2, data2 = cis.wavread('./samples/music2.wav')
rate3, data3 = cis.wavread('./samples/music3.wav')
if rate1 != rate2 or rate2 != rate3:
    raise ValueError('Sampling_rate_Error')

fs = rate1
x = np.array([data1, data2, data3], dtype=np.float32)
y = IVA(x, fs).iva()

cis.wavwrite('./samples/iva_1_out.wav', fs, y[0])
cis.wavwrite('./samples/iva_2_out.wav', fs, y[1])
cis.wavwrite('./samples/iva_3_out.wav', fs, y[2])