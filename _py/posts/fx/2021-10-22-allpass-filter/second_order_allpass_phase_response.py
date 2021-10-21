from fractions import Fraction
import numpy as np
import scipy.signal as sig
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path


def c_param(fb):
    return (np.tan(np.pi * fb) - 1) / (np.tan(np.pi * fb) + 1) # fs = 1

def d_param(fc):
    return - np.cos(2 * np.pi * fc) # fs = 1

if __name__ == '__main__':
    output_dir = Path('assets', 'img', 'posts', 'fx', '2021-10-22-allpass-filter')
    matplotlib.rcParams.update({'font.size': 16})
    matplotlib.rcParams.update({'lines.linewidth': 2})
    matplotlib.rcParams.update({'figure.autolayout': True})
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = ['Verdana']
    plot_dict = {"bbox_inches": 'tight', "dpi": 300, "transparent": True}

    cutoff_frequencies = [Fraction(1, 16), Fraction(1, 8), Fraction(3, 16)] # fs = 1
    # cutoff_frequencies = [Fraction(1, 8), Fraction(1, 8), Fraction(1, 8)] # fs = 1
    bandwidths = [0.022, 0.022, 0.022] # fs = 1
    # bandwidths = [0.022, 0.044, 0.088] # fs = 1

    line_styles = ['-', '--', '-.']

    fig, ax1 = plt.subplots()
    for fc, fb, line_style in zip(cutoff_frequencies, bandwidths, line_styles):
        c = c_param(fb)
        d = d_param(fc)

        b = [-c, d*(1-c), 1]
        a = [1,  d*(1-c), -c]

        w, h = sig.freqz(b, a, fs=1)
        
        angles = np.unwrap(np.angle(h))

        # ax1.set_title('Second-order allpass filter phase response')
        ax1.plot(w, angles, f'k{line_style}')
        ax1.set_ylabel('Phase shift [rad]')
        ax1.grid()
        ax1.axis('tight')

        ax1.vlines(x=float(fc), ymin=-7, ymax=-np.pi, color='b', linestyle='--')
    plt.legend([f'fc = {fc}' for fc in cutoff_frequencies])
    # plt.legend([f'fb = {fb}' for fb in bandwidths])
    plt.xlim([0, 0.5])
    plt.ylim([-2 * np.pi - 0.1, 0.1])
    plt.xlabel('fc / fs')
    plt.axhline(y=-np.pi, color='r')
    plt.savefig(output_dir / f'second_order_allpass_phase_response.png', **plot_dict)
