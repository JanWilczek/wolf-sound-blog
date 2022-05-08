#!/usr/bin/python3
from scipy import signal
import numpy as np
import soundfile as sf


def generate_white_noise(duration_in_seconds, sampling_rate):
    duration_in_samples = int(duration_in_seconds * sampling_rate)
    return np.random.default_rng().uniform(-1, 1, duration_in_samples)

def main():
    sampling_rate = 44100
    duration_in_seconds = 5
    white_noise = generate_white_noise(duration_in_seconds, sampling_rate)
    highpass = False
    amplitude = 0.1

    input_signal = white_noise

    cutoff_frequency = np.geomspace(20000, 20, input_signal.shape[0])

    # b = [a1, 1]
    # a = [1, a1]

    # allpass_output = signal.lfilter(b, a, input_signal)
    allpass_output = np.zeros_like(input_signal)
    dn_1 = 0
    for n in range(input_signal.shape[0]):
        break_frequency = cutoff_frequency[n]
        
        tan = np.tan(np.pi * break_frequency / sampling_rate)
        a1 = (tan - 1) / (tan + 1)

        allpass_output[n] = a1 * input_signal[n] + dn_1
        dn_1 = input_signal[n] - a1 * allpass_output[n]

    if highpass:
        allpass_output *= -1

    filter_output = input_signal + allpass_output
    filter_output *= 0.5
    filter_output *= amplitude

    filename = 'filtered_white_noise.flac'

    sf.write(filename, filter_output, sampling_rate)


if __name__ == '__main__':
    main()
