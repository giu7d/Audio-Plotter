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

time_dom = np.linspace(0, data_size / float(sample_rate), num=float(data_size))  # Linear Space [0-10] num=44100 * 10


plot.figure(1, figsize=(8, 8), dpi=80)
plot.subplot(211)
plot.plot(time_dom, channel[0], linewidth=1, alpha=0.8, color='blue')
plot.xlabel('Tempo (s)')
plot.ylabel('')
plot.subplot(212)
plot.plot(time_dom, channel[1], linewidth=1, alpha=0.8, color='orange')
plot.xlabel('Tempo (s)')
plot.ylabel('')

# Fourier Transformation Graph

fourier = fft.fft(channel)

plot.figure(2, figsize=(8, 8), dpi=80)
plot.subplot(211)
plot.plot(abs(fourier[0]), linewidth=1, alpha=0.8, color='blue')
plot.xlabel('abs(fft(x))')
plot.ylabel('')
plot.subplot(212)
plot.plot(abs(fourier[1]), linewidth=1, alpha=0.8, color='orange')
plot.xlabel('abs(fft(x))')
plot.ylabel('')

plot.show()



#
#
# #
#
# n = int(data_size/2)
#
# tmp = fourier[0]
# tmp = tmp[0:n]
# foo_l = tmp / float(data_size)
#
# tmp = fourier[1]
# tmp = tmp[0:n]
# foo_r = tmp / float(data_size)
#
#
# freq_array = np.arange(0, (data_size / 2), 1.0) * (sample_rate * 1.0 / data_size);
#
# plot.figure(3, figsize=(8, 8), dpi=80)
#
# plot.subplot(211)
# plot.plot(freq_array / 1000, 10 * np.log10(foo_l), color='blue', linewidth=0.02)
# plot.title('')
# plot.xlabel('Frequência (kHz)')
# plot.ylabel('Decibels (dB)')
#
# plot.subplot(212)
# plot.plot(freq_array / 1000, 10 * np.log10(foo_r), color='orange', linewidth=0.02)
# plot.xlabel('Frequência (kHz)')
# plot.ylabel('Decibels (dB)')
# plot.show()
#
# #
#
# plot.figure(4, figsize=(8,6))
#
# plot.subplot(211)
# Pxx, freqs, bins, im = plot.specgram(channel[0], Fs=sample_rate, NFFT=1024, cmap=plot.get_cmap('autumn_r'))
# cbar = plot.colorbar(im)
# plot.xlabel('Time (s)')
# plot.ylabel('Frequency (Hz)')
# cbar.set_label('Intensity dB')
# plot.subplot(212)
#
# Pxx, freqs, bins, im = plot.specgram(channel[1], Fs=sample_rate, NFFT=1024, cmap=plot.get_cmap('autumn_r'))
# cbar = plot.colorbar(im)
# plot.xlabel('Time (s)')
# plot.ylabel('Frequency (Hz)')
# cbar.set_label('Intensity (dB)')
# plot.show()
#
# #
#
#
# Pxx_l, freqs_l, bins_l, im = plot.specgram(channel[0], Fs=sample_rate, NFFT=1024, noverlap=0, cmap=plot.get_cmap('autumn_r'))
# np.where(freqs_l == 10034.47265625)
# hz_l = Pxx_l[233,:]
#
# Pxx_r, freqs_r, bins_r, im = plot.specgram(channel[1], Fs=sample_rate, NFFT=1024, noverlap=0, cmap=plot.get_cmap('autumn_r'))
# np.where(freqs_r == 10034.47265625)
# hz_r = Pxx_r[233,:]
#
# plot.figure(4, figsize=(8,6))
# plot.subplot(211)
# plot.plot(bins_l, hz_l, color='blue')
# # plot.xlabel('Time (s)')
# # plot.ylabel('Frequency (Hz)')
#
# plot.subplot(212)
# plot.plot(bins_r, hz_r, color='orange')
# # plot.xlabel('Time (s)')
# # plot.ylabel('Frequency (Hz)')
# plot.show()
#
