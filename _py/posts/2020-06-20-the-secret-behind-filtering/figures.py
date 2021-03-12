#!/usr/bin/python
import numpy as np
import numpy.matlib as mtlb
import matplotlib.pyplot as plt
from pathlib import Path
import mpl_toolkits.mplot3d.art3d as art3d


COLORS = ['C0','C1','C2','C3']


def get_assets_path():
    path = Path.cwd()
    if (path / 'assets').is_dir():
        return path
    while path.name != '_py':
        path = path.parent
    return path.parent

def plot_signal(signal, filepath, color='k'):
    xlim = [-1, 7]

    plt.figure()
    plt.stem(signal, use_line_collection=True, basefmt=' ', markerfmt=f'{color}o', linefmt=f'{color}-')
    plt.xlim(xlim)
    plt.xlabel('$n$')
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
    plt.savefig(filepath.absolute(), bbox_inches='tight', dpi=300)
    # plt.show()

def plot_signals(signals, filepath):
    xlim = [-1, 7]


    plt.figure()
    for i in range(signals.shape[0]):
        plt.stem([i], [signals[i,i]], use_line_collection=True, basefmt=' ', markerfmt=f'{COLORS[i]}o', linefmt=f'{COLORS[i]}-')
    plt.xlim(xlim)
    plt.ylim([-1.1, 1.1])
    plt.xlabel('$n$')
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
    plt.savefig(filepath.absolute(), bbox_inches='tight', dpi=300)
    # plt.show()

def plot_signals_3d(signals, filepath):
    xlim = [-1, 7]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.view_init(20, 250)
    for i in range(signals.shape[0]):
        depth = 0.2* (i - 1)
        for j in range(signals.shape[1]):
            line = art3d.Line3D(*zip((j, depth, 0), (j, depth, signals[i,j])), marker='o', markevery=(1, 1), linestyle='-', color=COLORS[i])
            ax.add_line(line)
    plt.xlim(xlim)
    plt.xlabel('$n$')
    # plt.ylim([-1.1, 1.1])
    ax.set_yticklabels([])
    ax.set_ylim([-0.4, 0.5])
    ax.set_zlim([0,0.6])
    # ax.set_zticks(np.arange(-1,1.1,0.25))
    # ax.set_zticklabels(['-1','','','','0','','','','1'])

    plt.savefig(filepath.absolute(), bbox_inches='tight', dpi=300)
    # plt.show()

def main():
    assets_path = get_assets_path()
    post_images_path = assets_path.joinpath('assets/img/posts/2020-06-20-the-secret-behind-filtering')

    x = np.array([0.8, 0.3, -0.6, 0.5])
    h = np.array([0.7, 0.2, 0.7])

    y = np.convolve(x, h)

    plot_signal(x, post_images_path.joinpath('x.png'))
    plot_signal(h, post_images_path.joinpath('h.png'))
    plot_signal(y, post_images_path.joinpath('y.png'))

    x_single = np.zeros((len(x),len(x)))
    for i in range(len(x)):
        x_single[i,i] = x[i]

    plot_signals(x_single, post_images_path.joinpath('x_single.png'))

    h_single = np.zeros((len(x),len(y)))
    for i in range(len(x)):
        h_single[i,:] = np.convolve(x_single[i,:],h)
        plot_signal(h_single[i,:], post_images_path.joinpath(f'h_single_{i}.png'), color=COLORS[i])

    
    plot_signals_3d(h_single, post_images_path.joinpath('h_superposed.png'))

    h_summed = np.sum(h_single, axis=0)
    plot_signal(h_summed, post_images_path.joinpath('h_summed.png'))
        

if __name__ == '__main__':
    main()
