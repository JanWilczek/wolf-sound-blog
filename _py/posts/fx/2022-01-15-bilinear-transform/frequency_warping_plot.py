from fractions import Fraction
import numpy as np
from numpy.polynomial.polynomial import Polynomial
import scipy.signal as sig
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path


if __name__ == '__main__':
    output_dir = Path('assets', 'img', 'posts', 'fx', '2022-01-15-bilinear-transform')
    matplotlib.rcParams.update({'font.size': 16})
    matplotlib.rcParams.update({'lines.linewidth': 2})
    matplotlib.rcParams.update({'figure.autolayout': True})
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = ['Verdana']
    plot_dict = {"bbox_inches": 'tight', "dpi": 300, "transparent": True}

    fs = 44100.0
    fs = 1

    xmin = -10
    xmax = -xmin
    omega_a = np.arange(xmin, xmax, 0.5)
    omega_d = 2 * fs * np.arctan(omega_a / (2 * fs))

    # Butterworth filters comparison
    plt.figure()
    title = 'FrequencyWarping'
    plt.ylim([ - 2 * np.pi, 2 * np.pi])
    plt.yticks([-np.pi, 0, np.pi], ['$-\pi$','0','$\pi$'])
    plt.hlines(-np.pi, xmin, xmax, colors='k', linestyles='--')
    plt.hlines(np.pi, xmin, xmax, colors='k', linestyles='--')
    plt.axhline(0, color='k')
    plt.axvline(0, color='k')
    plt.xlabel(r'$\omega_a$ [rad/s]')
    plt.ylabel(r'$\omega_d$ [rad/s]')
    plt.plot(omega_a, omega_d, color='#Ef7600')
    plt.savefig(output_dir / f'{title}.png', **plot_dict)
