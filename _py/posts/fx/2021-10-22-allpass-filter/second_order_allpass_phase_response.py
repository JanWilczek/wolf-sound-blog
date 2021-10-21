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
    matplotlib.rcParams.update({'font.size': 18})
    matplotlib.rcParams.update({'lines.linewidth': 4})
    matplotlib.rcParams.update({'figure.autolayout': True})
    matplotlib.rcParams['font.family'] = 'sans-serif'
    matplotlib.rcParams['font.sans-serif'] = ['Verdana']
    plot_dict = {"bbox_inches": 'tight', "dpi": 300}

    cutoff_frequencies = [1 / 16, 1/8, 3 / 16] # fs = 1
    bandwidths = [0.022, 0.022, 0.022] # fs = 1

    fig, ax1 = plt.subplots()
    for fc, fb in zip(cutoff_frequencies, bandwidths):
        c = c_param(fb)
        d = d_param(fc)

        b = [-c, d*(1-c), 1]
        a = [1,  d*(1-c), -c]

        w, h = sig.freqz(b, a, fs=1)
        
        angles = np.unwrap(np.angle(h))

        ax1.set_title('Second-order allpass filter phase response')
        ax1.plot(w, angles, 'g')
        ax1.set_ylabel('Angle (radians)', color='g')
        ax1.grid()
        ax1.axis('tight')
    plt.xlim([0, 0.5])
    plt.savefig(output_dir / f'second_order_allpass_phase_response.png', **plot_dict)
