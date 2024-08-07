import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from pathlib import Path
import argparse


def stem(n, x, filename, color='C0', xlabel='', ylabel='', yticks=None, video=False):
    plot_dict = {"bbox_inches": 'tight', "dpi": 300, "transparent": True}
    output_dir = Path('assets', 'img', 'posts', '2021-07-09-convolution-in-matlab-numpy-and-scipy')
    if video:
        output_dir /= 'video'
    output_dir.mkdir(parents=True, exist_ok=True)

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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--video', action='store_true', help='Export for video.')
    args = ap.parse_args()

    matplotlib.rcParams.update({'font.size': 20})
    matplotlib.rcParams.update({'lines.linewidth': 4})
    matplotlib.rcParams.update({'figure.autolayout': True})
    if args.video:
        plt.style.use('dark_background')

    yticks = [-1.0, 0.0, 1.0]

    N = 10
    n_x = np.arange(0, 2 * N)
    x = np.sin(2 * np.pi * n_x / 20 + 0.1)
    n_y = np.arange(0, N)
    y = np.exp(0.05 * n_y) - 1.4

    stem(n_x, x, 'x', xlabel='n', ylabel='x[n]', video=args.video)
    stem(n_y, y, 'y', xlabel='n', ylabel='y[n]', color='C1', video=args.video)

    full = np.convolve(x, y, 'full')
    n_full = np.arange(0, full.shape[0], dtype=int)
    valid = np.convolve(x, y, 'valid')
    n_valid = np.arange(0, valid.shape[0], dtype=int)
    same = np.convolve(x, y, 'same')
    n_same = np.arange(0, same.shape[0], dtype=int)

    valid_start_id = 9
    padded_valid = np.zeros_like(full)
    padded_valid[valid_start_id:valid_start_id + N + 1] = valid

    stem(n_full, full, 'xy_full', xlabel='n', ylabel=r'$(x \ast y)_{full}$[n]', color='C2', video=args.video)
    stem(n_valid, valid, 'xy_valid', xlabel='n', ylabel=r'$(x \ast y)_{valid}$[n]', color='C3', video=args.video)
    stem(n_same, same, 'xy_same', xlabel='n', ylabel=r'$(x \ast y)_{same}$[n]', color='C4', video=args.video)


if __name__ == '__main__':
    main()
