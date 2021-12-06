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

    # Butterworth filters comparison
    plt.figure()
    title = 'ButterworthComparison'

    orders = [2, 4, 11]
    line_styles = ['-', '--', '-.']

    legend = []

    b = [1]
    for order, line_style in zip(orders, line_styles):
        a = butterworth_denominator_coefficients(order)
        w, h = sig.freqs(b, a, worN=np.logspace(-1, 2, 1000))
        # plt.semilogx(w, 20 * np.log10(abs(h)))
        plt.semilogx(w, abs(h), line_style)
        legend.append(f'$N={order}$')
    plt.semilogx(w, ideal_lowpass_amplitude_response(w, 1), ':')
    legend.append('ideal')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude response')
    plt.grid()
    plt.xlim([0.1, 100])
    plt.xticks([0.1, 1, 10], ['0.1', r'$\omega_a = 1$', '10'])
    plt.legend(legend)
    plt.savefig(output_dir / f'{title}.png', **plot_dict)

    # Butterworth filters comparison in decibels
    plt.figure()
    title = 'ButterworthComparisonDecibels'

    legend = []

    for order, line_style in zip(orders, line_styles):
        a = butterworth_denominator_coefficients(order)
        w, h = sig.freqs(b, a, worN=np.logspace(-1, 2, 1000))
        plt.semilogx(w, 20 * np.log10(abs(h)), line_style)
        legend.append(f'$N={order}$')
    plt.semilogx(w, 20 * np.log10(np.maximum(ideal_lowpass_amplitude_response(w, 1), 1e-6)), ':')
    legend.append('ideal')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude response [dB]')
    plt.grid()
    plt.xlim([0.1, 100])
    plt.ylim([-60,1])
    plt.xticks([0.1, 1, 10], ['0.1', r'$\omega_a = 1$', '10'])
    plt.legend(legend)
    plt.savefig(output_dir / f'{title}.png', **plot_dict)

    # Ideal low-pass
    plt.figure()
    title = 'IdealLowPass'
    plt.semilogx(w, ideal_lowpass_amplitude_response(w, 1), 'C3')
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude response')
    plt.grid()
    plt.xlim([0.1, 100])
    plt.xticks([0.1, 1, 10], ['0.1', r'$\omega_a = 1$', '10'])
    plt.savefig(output_dir / f'{title}.png', **plot_dict)

