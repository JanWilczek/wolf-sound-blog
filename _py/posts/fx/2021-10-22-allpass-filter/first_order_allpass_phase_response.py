from fractions import Fraction
import numpy as np
import scipy.signal as sig
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path


def a_coeff(fb):
    return (np.tan(np.pi * fb) - 1) / (np.tan(np.pi * fb) + 1) # fs = 1


if __name__ == '__main__':
    output_dir = Path('assets', 'img', 'posts', 'fx', '2021-10-22-allpass-filter')
    matplotlib.rcParams.update({'font.size': 16})
    matplotlib.rcParams.update({'lines.linewidth': 2})
    matplotlib.rcParams.update({'figure.autolayout': True})
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = ['Verdana']
    plot_dict = {"bbox_inches": 'tight', "dpi": 300, "transparent": True}

    break_frequencies = [Fraction(1, 16), Fraction(1, 8), Fraction(3, 16)] # fs = 1

    line_styles = ['-', '--', '-.']

    fig, ax1 = plt.subplots()
    for fb, line_style in zip(break_frequencies, line_styles):
        a1 = a_coeff(fb)

        b = [a1, 1]
        a = [1, a1]

        w, h = sig.freqz(b, a, fs=1)
        
        angles = np.unwrap(np.angle(h))

        ax1.plot(w, angles, f'k{line_style}')
        ax1.set_ylabel('Phase shift [rad]')
        ax1.grid()
        ax1.axis('tight')

        ax1.vlines(x=float(fb), ymin=-3.4, ymax=-np.pi / 2, color='b', linestyle='--')
    plt.legend([r'$f_b / f_s = $' + str(fb) for fb in break_frequencies])
    plt.xlim([0, 0.5])
    plt.ylim([-np.pi - 0.1, 0.1])
    plt.xlabel('f / fs')
    plt.yticks([0, -np.pi/4, -np.pi/2, -3 * np.pi/4, -np.pi], ['0', '$-\pi/4$', '$-\pi/2$', '$-3\pi/4$', '$-\pi$'])
    plt.axhline(y=-np.pi/2, color='r')
    plt.savefig(output_dir / f'first_order_allpass_phase_response.png', **plot_dict)
