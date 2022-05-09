#!/usr/bin/python3
from scipy import signal
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path
import subprocess
from allpass_based_lowpass_and_highpass_filters import allpass_filter


def waveform_misalignment_example():
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

    sine_length = 1024

    x = np.zeros((3*sine_length,))
    sines_arg = np.linspace(0, 2 * np.pi, sine_length)
    sines = np.sin(sines_arg) + np.sin(2 * sines_arg) + np.sin(3 * sines_arg)
    x[:sine_length] = sines
    x = np.roll(x, sine_length)
    y = allpass_filter(x, 20 * np.ones_like(x), sampling_rate)

    plt.figure()
    plt.subplot(121)
    plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,
    right=False,
    labelleft=False,
    labelbottom=False) # labels along the bottom edge are off
    plt.plot(x, color='#Ef7600')
    plt.ylabel('Amplitude')
    plt.ylim([-2.7, 2.7])
    plt.subplot(122)
    plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,
    right=False,
    labelleft=False,
    labelbottom=False) # labels along the bottom edge are off
    plt.plot(y, color='#Ef7600')
    plt.ylim([-2.7, 2.7])
    output_path = output_dir / f'aligned_sines.png'
    plt.savefig(output_path, **plot_dict)

    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])


def main():
    waveform_misalignment_example()


if __name__ == '__main__':
    main()

