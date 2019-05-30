import numpy as np
import sys
import scipy.io.wavfile as wf
from fastAuxIVA import AuxIVA
from sound_mixing import Preprocessing

#prepare data
rate1, data1 = wf.read('./samples/fmix_1.wav')
rate2, data2 = wf.read('./samples/fmix_2.wav')
rate3, data3 = wf.read('./samples/fmix_3.wav')
if rate1 != rate2 or rate2 != rate3:
    raise ValueError('Sampling_rate_Error')

x = np.vstack([data1.astype(float), data2.astype(float), data3.astype(float)])

y = AuxIVA(x, sample_freq=rate1,beta=0.1).auxiva()

y = [(y_i * 32767 / max(np.absolute(y_i))).astype(np.int16) for y_i in np.asarray(y)]

wf.write('./samples/fmix_1_out_1.wav', rate1, y[0])
wf.write('./samples/fmix_2_out_1.wav', rate2, y[1])
wf.write('./samples/fmix_3_out_1.wav', rate3, y[2])

x = np.vstack([data1.astype(float), data2.astype(float), data3.astype(float)])

y = AuxIVA(x, sample_freq=rate1,beta=0.2).auxiva()

y = [(y_i * 32767 / max(np.absolute(y_i))).astype(np.int16) for y_i in np.asarray(y)]

wf.write('./samples/fmix_1_out_2.wav', rate1, y[0])
wf.write('./samples/fmix_2_out_2.wav', rate2, y[1])
wf.write('./samples/fmix_3_out_2.wav', rate3, y[2])

x = np.vstack([data1.astype(float), data2.astype(float), data3.astype(float)])

y = AuxIVA(x, sample_freq=rate1,beta=0.3).auxiva()

y = [(y_i * 32767 / max(np.absolute(y_i))).astype(np.int16) for y_i in np.asarray(y)]

wf.write('./samples/fmix_1_out_3.wav', rate1, y[0])
wf.write('./samples/fmix_2_out_3.wav', rate2, y[1])
wf.write('./samples/fmix_3_out_3.wav', rate3, y[2])

x = np.vstack([data1.astype(float), data2.astype(float), data3.astype(float)])

y = AuxIVA(x, sample_freq=rate1,beta=0.4).auxiva()

y = [(y_i * 32767 / max(np.absolute(y_i))).astype(np.int16) for y_i in np.asarray(y)]

wf.write('./samples/fmix_1_out_4.wav', rate1, y[0])
wf.write('./samples/fmix_2_out_4.wav', rate2, y[1])
wf.write('./samples/fmix_3_out_4.wav', rate3, y[2])

x = np.vstack([data1.astype(float), data2.astype(float), data3.astype(float)])

y = AuxIVA(x, sample_freq=rate1,beta=0.5).auxiva()

y = [(y_i * 32767 / max(np.absolute(y_i))).astype(np.int16) for y_i in np.asarray(y)]

wf.write('./samples/fmix_1_out_5.wav', rate1, y[0])
wf.write('./samples/fmix_2_out_5.wav', rate2, y[1])
wf.write('./samples/fmix_3_out_5.wav', rate3, y[2])