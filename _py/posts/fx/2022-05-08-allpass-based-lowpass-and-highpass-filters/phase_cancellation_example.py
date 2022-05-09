#!/usr/bin/python3
from scipy import signal
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path
import subprocess


def waveform_misalignment_example():
    output_dir = Path('assets', 'img', 'posts', 'fx', '2022-05-08-allpass-based-lowpass-and-highpass-filters')
    output_dir.mkdir(parents=True, exist_ok=True)
    matplotlib.rcParams.update({'font.size': 16})
    matplotlib.rcParams.update({'lines.linewidth': 2})
    matplotlib.rcParams.update({'figure.autolayout': True})
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = ['Verdana']
    plot_dict = {"bbox_inches": 'tight', "dpi": 300, "transparent": True}

    sine_length = 1024
    sines_arg = np.linspace(0, 6 * np.pi, 3 * sine_length)
    sine = np.sin(sines_arg)
    inverted_sine = -1 * sine
    superposition = sine + inverted_sine

    plt.figure()
    plt.subplot(311)
    plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,
    right=False,
    labelleft=False,
    labelbottom=False) # labels along the bottom edge are off
    plt.plot(sine, color='C0')
    plt.gca().axis('off')
    plt.subplot(312)
    plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,
    right=False,
    labelleft=False,
    labelbottom=False) # labels along the bottom edge are off
    plt.gca().axis('off')
    plt.plot(inverted_sine, color='C1')
    plt.subplot(313)
    plt.plot(sine, linestyle='--', alpha=0.5)
    plt.plot(inverted_sine, linestyle='--', alpha=0.5)
    plt.plot(superposition, color='#Ef7600')
    plt.gca().axis('off')
    plt.tick_params(
    axis='both',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom=False,      # ticks along the bottom edge are off
    top=False,         # ticks along the top edge are off
    left=False,
    right=False,
    labelleft=False,
    labelbottom=False) # labels along the bottom edge are off
    output_path = output_dir / f'phase_cancellation_example.png'
    plt.savefig(output_path, **plot_dict)

    subprocess.run(['cwebp', '-q', '65', '-resize', '800', '0', output_path, '-o', output_path.with_suffix('.webp')])


def main():
    waveform_misalignment_example()


if __name__ == '__main__':
    main()

