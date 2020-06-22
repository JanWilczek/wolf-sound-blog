#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


IMG_DIR = '../..'

x = np.array([0.1, 0.6, 0.4, 0.2])
h = np.array([0.7, 0.5, 0.3])

def get_assets_path():
    path = Path.cwd()
    while path.name != 'assets':
        path = path.parent
    return path

def plot_signal(signal, filepath):
    xlim = [-1, 7]

    plt.figure()
    plt.stem(x, use_line_collection=True, basefmt=' ', markerfmt='ok', linefmt='k-')
    plt.xlim(xlim)
    plt.ylim([-1.1, 1.1])
    plt.yticks(np.arange(-1,1.1,0.25), labels=['-1','','','','0','','','','1'])
    # plt.grid(b=True)
    ax = plt.gca()
    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    ax.spines['left'].set_position(('data', 0.0))
    ax.spines['bottom'].set_position(('data', 0.0))

    # Eliminate upper and right axes
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    # plt.savefig(filepath.absolute(), bbox_inches='tight', dpi=300)
    plt.show()

def main():
    assets_path = get_assets_path()
    post_images_path = assets_path.joinpath('/img/posts/2020-06-20-the-secret-behind-filtering')
    filepath = post_images_path.joinpath('x.png')

    y = np.convolve(x, h)

    plot_signal(x, filepath)

    

if __name__ == '__main__':
    main()
