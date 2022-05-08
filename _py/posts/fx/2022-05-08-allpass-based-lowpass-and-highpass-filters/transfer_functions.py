#!/usr/bin/python3
from scipy import signal
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path
import subprocess
from allpass_based_lowpass_and_highpass_filters import a1_coefficient


def lowpass_freqz(cutoff_frequency, sampling_rate):
    a1 = a1_coefficient(cutoff_frequency, sampling_rate)

    b = 0.5 * np.array([1 + a1, 1 + a1])
    a = [1, a1]

    return signal.freqz(b, a, fs=sampling_rate)


def highpass_freqz(cutoff_frequency, sampling_rate):
    a1 = a1_coefficient(cutoff_frequency, sampling_rate)

    b = 0.5 * np.array([-1 + a1, 1 - a1])
    a = [1, a1]

    return signal.freqz(b, a, fs=sampling_rate)


def plot_transfer_functions(freqz_function, name):
    output_dir = Path('assets', 'img', 'posts', 'fx', '2022-05-08-allpass-based-lowpass-and-highpass-filters')
    output_dir.mkdir(parents=True, exist_ok=True)
    matplotlib.rcParams.update({'font.size': 16})
    matplotlib.rcParams.update({'lines.linewidth': 2})
    matplotlib.rcParams.update({'figure.autolayout': True})
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = ['Verdana']
    plot_dict = {"bbox_inches": 'tight', "dpi": 300, "transparent": True}

    sampling_rate = 44100
    cutoff_frequency = 500.0

    plt.figure()

    plt.vlines(x=cutoff_frequency, ymin=-60, ymax=-3, colors='k', linestyles='--')
    plt.hlines(y=-3, xmin=0, xmax=cutoff_frequency, colors='k', linestyles='--')
    
    w, h = freqz_function(cutoff_frequency, sampling_rate)
    magnitude_db = 20 * np.log10(np.maximum(np.abs(h), 1e-5))
    plt.semilogx(np.maximum(1e-5, w), magnitude_db, color='#Ef7600')

    plt.xlim([50, 22000])
    plt.xticks([125, 250, 500, 1000, 2000, 4000, 8000, 16000], ['125', '250', '500', '1k', '2k', '4k', '8k', '16k'])
    plt.ylim([-30, 1])
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude [dB]')
    output_path = output_dir / f'{name}_transfer_function.png'
    plt.savefig(output_path, **plot_dict)

    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])


def main():
    for freqz_function, name in zip([lowpass_freqz, highpass_freqz], ['lowpass', 'highpass']):
        plot_transfer_functions(freqz_function, name)


if __name__ == '__main__':
    main()

