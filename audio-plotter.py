#!/usr/bin/env python

import matplotlib.pyplot as plot
import numpy as np
from numpy import fft
import wave
import sys


try:
    wav_file = wave.open(sys.argv[1], 'r')
    # wav_file = wave.open('the_less_i_know_the_better.wav', 'r')
except FileNotFoundError:
    print(FileNotFoundError)


data_size = wav_file.getnframes()                   # (Hz * s)
sample_rate = wav_file.getframerate()               # Freq. (Hz)

sound_data = wav_file.readframes(data_size)         # File Binary
sound_signal = np.fromstring(sound_data, 'Int16')   # File Array
channel = [[] for channel in range(wav_file.getnchannels())]

for i, value in enumerate(sound_signal):
    channel[i % len(channel)].append(value)


# Time Domain Graph

time_dom = np.linspace(0, data_size / float(sample_rate), num=float(data_size))  # Linear Space [0-10] num = 44100 * 10

plot.figure(1, figsize=(8, 8), dpi=80)
plot.subplots_adjust(hspace = 0.5)
plot.subplot(211)
plot.title('SINAL NO DOMÍNIO DO TEMPO\n\nCanal 1\n')
plot.plot(time_dom, channel[0], linewidth=1, alpha=0.8, color='blue')
plot.xlabel('\nTempo (s)')
# plot.ylabel('Amplitude')
plot.subplot(212)
plot.title('Canal 2\n')
plot.plot(time_dom, channel[1], linewidth=1, alpha=0.8, color='orange')
plot.xlabel('\nTempo (s)')
# plot.ylabel('Amplitude')

# Fourier Transformation Graph

fourier = fft.fft(channel)

plot.figure(2, figsize=(8, 8), dpi=80)
plot.subplots_adjust(hspace = 0.5)
plot.subplot(211)
plot.title('SINAL NO DOMÍNIO DA FREQUÊNCIA\n\nCanal 1\n')
plot.plot(abs(fourier[0]), linewidth=1, alpha=0.8, color='blue')
plot.xlabel('\nFrequência (Hz)')
# plot.ylabel('Amplitude')
plot.subplot(212)
plot.title('Canal 2\n')
plot.plot(abs(fourier[1]), linewidth=1, alpha=0.8, color='orange')
plot.xlabel('\nFrequência (Hz)')
# plot.ylabel('Amplitude')

plot.show()