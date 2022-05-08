#!/usr/bin/python3
from scipy import signal
import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt


def generate_white_noise(duration_in_seconds, sampling_rate):
    duration_in_samples = int(duration_in_seconds * sampling_rate)
    return np.random.default_rng().uniform(-1, 1, duration_in_samples)

def a1_coefficient(break_frequency, sampling_rate):
    tan = np.tan(np.pi * break_frequency / sampling_rate)
    return (tan - 1) / (tan + 1)

def allpass_filter(input_signal, break_frequency, sampling_rate):
    allpass_output = np.zeros_like(input_signal)
    dn_1 = 0
    for n in range(input_signal.shape[0]):
        a1 = a1_coefficient(break_frequency[n], sampling_rate)

        allpass_output[n] = a1 * input_signal[n] + dn_1
        dn_1 = input_signal[n] - a1 * allpass_output[n]
    return allpass_output

def allpass_based_filter(input_signal, cutoff_frequency, sampling_rate, highpass=False, amplitude=1.0):
    allpass_output = allpass_filter(input_signal, cutoff_frequency, sampling_rate)

    if highpass:
        allpass_output *= -1

    filter_output = input_signal + allpass_output
    filter_output *= 0.5
    filter_output *= amplitude

    return filter_output

def white_noise_filtering_example():
    sampling_rate = 44100
    duration_in_seconds = 5
    white_noise = generate_white_noise(duration_in_seconds, sampling_rate)
    input_signal = white_noise

    cutoff_frequency = np.geomspace(20000, 20, input_signal.shape[0])

    filter_output = allpass_based_filter(input_signal, cutoff_frequency, sampling_rate, highpass=False, amplitude=0.1)

    filename = 'filtered_white_noise.flac'

    sf.write(filename, filter_output, sampling_rate)

def plot_transfer_functions():
    sampling_rate = 44100
    cutoff_frequency = 500.0

    a1 = a1_coefficient(cutoff_frequency, sampling_rate)

    b = [1 + a1, 1 + a1]
    a = [1, a1]

    w, h = signal.freqz(b, a, fs=sampling_rate)

    plt.figure()
    plt.semilogx(np.maximum(1e-5, w), np.abs(h))
    plt.xlim([10, 10000])
    plt.savefig('lowpass_transfer_function.png', dpi=100)


def main():
    # white_noise_filtering_example()
    plot_transfer_functions()


if __name__ == '__main__':
    main()
