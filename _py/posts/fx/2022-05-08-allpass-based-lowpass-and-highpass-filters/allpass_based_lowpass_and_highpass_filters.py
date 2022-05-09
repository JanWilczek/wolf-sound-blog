#!/usr/bin/python3
from scipy import signal
import numpy as np
import soundfile as sf
from pathlib import Path


def generate_white_noise(duration_in_seconds, sampling_rate):
    duration_in_samples = int(duration_in_seconds * sampling_rate)
    return np.random.default_rng().uniform(-1, 1, duration_in_samples)


def a1_coefficient(break_frequency, sampling_rate):
    tan = np.tan(np.pi * break_frequency / sampling_rate)
    return (tan - 1) / (tan + 1)


def allpass_filter(input_signal, break_frequency, sampling_rate):
    # Initialize the output array
    allpass_output = np.zeros_like(input_signal)

    # Initialize the inner 1-sample buffer
    dn_1 = 0

    for n in range(input_signal.shape[0]):
        # The allpass coefficient is computed for each sample
        # to show its adaptability
        a1 = a1_coefficient(break_frequency[n], sampling_rate)

        # The allpass difference equation
        # Check the article on the allpass filter for an 
        # in-depth explanation
        allpass_output[n] = a1 * input_signal[n] + dn_1

        # Store a value in the inner buffer for the 
        # next iteration
        dn_1 = input_signal[n] - a1 * allpass_output[n]
    return allpass_output


def allpass_based_filter(input_signal, cutoff_frequency, \
    sampling_rate, highpass=False, amplitude=1.0):
    # Perform allpass filtering
    allpass_output = allpass_filter(input_signal, \
        cutoff_frequency, sampling_rate)

    # If we want a highpass, we need to invert 
    # the allpass output in phase
    if highpass:
        allpass_output *= -1

    # Sum the allpass output with the direct path
    filter_output = input_signal + allpass_output

    # Scale the amplitude to prevent clipping
    filter_output *= 0.5

    # Apply the given amplitude
    filter_output *= amplitude

    return filter_output


def white_noise_filtering_example():
    sampling_rate = 44100
    duration_in_seconds = 5

    # Generate 5 seconds of white noise
    white_noise = generate_white_noise(duration_in_seconds, sampling_rate)
    input_signal = white_noise

    # Make the cutoff frequency decay with time ("real-time control")
    cutoff_frequency = np.geomspace(20000, 20, input_signal.shape[0])

    # Actual filtering
    filter_output = allpass_based_filter(input_signal, \
        cutoff_frequency, sampling_rate, highpass=False, amplitude=0.1)

    # Store the result in a file
    output_dir = Path('assets', 'wav', 'posts', 'fx', \
        '2022-05-08-allpass-based-lowpass-and-highpass-filters')
    output_dir.mkdir(parents=True, exist_ok=True)
    filename = 'filtered_white_noise.flac'
    sf.write(output_dir / filename, filter_output, sampling_rate)


def main():
    white_noise_filtering_example()


if __name__ == '__main__':
    main()
