from fractions import Fraction
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import scipy.signal as sig
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path


def butterworth_denominator_coefficients(order):
    assert order >= 1
    denominator = Polynomial([1])
    if order % 2 == 0:
        for m in range(1, order, 2):
            denominator *= Polynomial([1, 2 * np.cos(m * np.pi / (2 * order)), 1])
    else:
        denominator *= Polynomial([1, 1])
        for k in range(1, (order-1)//2 + 1):
            denominator *= Polynomial([1, 2 * np.cos(2 * k * np.pi / (2 * order)), 1])
    return list(denominator)

def ideal_lowpass_amplitude_response(frequencies, cutoff_frequency):
    h = np.ones_like(frequencies)
    h[frequencies > cutoff_frequency] = 0.0
    return h

if __name__ == '__main__':
    output_dir = Path('assets', 'img', 'posts', 'fx', '2021-12-03-analog-prototype')
    matplotlib.rcParams.update({'font.size': 16})
    matplotlib.rcParams.update({'lines.linewidth': 2})
    matplotlib.rcParams.update({'figure.autolayout': True})
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = ['Verdana']
    plot_dict = {"bbox_inches": 'tight', "dpi": 300, "transparent": True}

    title = 'ButterworthComparison'

    b = [1]
    for order in [2, 4, 12]:
        a = butterworth_denominator_coefficients(order)
        w, h = sig.freqs(b, a, worN=np.logspace(-1, 2, 1000))
        # plt.semilogx(w, 20 * np.log10(abs(h)))
        plt.semilogx(w, abs(h))
    plt.semilogx(w, ideal_lowpass_amplitude_response(w, 1))
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude response')
    plt.grid()
    plt.xlim([0.1, 100])
    # plt.xticks([1], ['1'])
    plt.xticks([1], [r'$\omega_a$'])
    plt.savefig(output_dir / f'{title}.png', **plot_dict)
