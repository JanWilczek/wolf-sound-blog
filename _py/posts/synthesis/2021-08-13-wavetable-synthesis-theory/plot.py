import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from pathlib import Path


def setup_pyplot_for_latex():
    # Use LaTeX font to save the figures in the .png format
    # (they are too big for a tikzfigure)
    matplotlib.rc('text', usetex=True)
    matplotlib.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})
    plt.rcParams.update({'font.size': 20})

def stem(n, x, filename, output_dir, color='C0', xlabel='', ylabel='', yticks=None, video=False):
    plot_dict = {"bbox_inches": 'tight', "dpi": 300, "transparent": True}
    if video:
        output_dir /= 'video'
    output_dir.mkdir(parents=True, exist_ok=True)

    matplotlib.rcParams.update({'font.size': 20})
    matplotlib.rcParams.update({'lines.linewidth': 4})
    matplotlib.rcParams.update({'figure.autolayout': True})
    if video:
        plt.style.use('dark_background')

    plt.figure()
    markerline, stemlines, baseline = plt.stem(n, x)
    plt.setp(markerline, 'color', color)
    plt.setp(stemlines, 'color', color)
    if video:
        plt.setp(baseline, 'color', 'white')
    else:
        plt.setp(baseline, 'color', 'k')
    plt.setp(baseline, 'linewidth', 0.5)
    plt.setp(baseline, 'zorder', -1)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.yticks(yticks)
    plt.savefig(output_dir / f'{filename}.png', **plot_dict)

def plot(n, x, filename, output_dir, color='C0', xlabel='', ylabel='', yticks=None, ylim=None, xlim=None, logscale=False, xticks=None):
    plot_dict = {"bbox_inches": 'tight', "dpi": 300, "transparent": True}
    output_dir.mkdir(parents=True, exist_ok=True)

    matplotlib.rcParams.update({'font.size': 20})
    matplotlib.rcParams.update({'lines.linewidth': 4})
    matplotlib.rcParams.update({'figure.autolayout': True})

    plt.figure()
    plt.plot(n, x, color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.yticks(yticks)
    if ylim:
        plt.ylim(ylim)
    if xlim:
        plt.xlim(xlim)
    if logscale:
        plt.xscale("log")
    if xticks:
        plt.xticks(xticks, [str(tick) for tick in xticks])
    plt.savefig(output_dir / f'{filename}.png', **plot_dict)

def normalized(signal):
    """Return rescaled signal so that it is in the [-1,1] range."""
    return signal / np.amax(np.abs(signal))


def magnitude_spectrum(time_signal, dB=True, normalize_spectrum=False):
    """Return magnitude spectrum of the real-valued time_signal.
    If dB is True, convert to decibel scale.
    Do not return the reflected part of the spectrum."""
    spectrum = np.fft.rfft(time_signal, axis=0)
    magnitude = np.abs(spectrum)
    if normalize_spectrum:
        magnitude = normalized(magnitude)
    if dB:
        return amplitude2dB(magnitude)
    return magnitude

def amplitude2dB(signal):
    """Convert the linear amplitude to an amplitude in decibels."""
    return 20 * np.log10(np.maximum(signal, 1e-7))
