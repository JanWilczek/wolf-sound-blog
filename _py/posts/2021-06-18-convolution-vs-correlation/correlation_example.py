import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import animation
from pathlib import Path


def main():
    matplotlib.rcParams.update({'font.size': 14})
    matplotlib.rcParams.update({'lines.linewidth': 4})
    plot_dict = {"bbox_inches": 'tight', "dpi": 300}
    yticks = [-1.0, 0.0, 1.0]
    output_dir = Path('assets/img/posts/2021-06-18-convolution-vs-correlation')
    N = 20
    n = np.arange(-N, N)
    x = np.sin(2 * np.pi * n / 20)
    y = np.exp(0.05 * n) - 1.4

    plt.figure()
    # plt.plot(n, x)
    markerline, stemlines, baseline = plt.stem(n, x, basefmt=' ')
    plt.setp(markerline, 'color', 'C0')
    plt.setp(stemlines, 'color', 'C0')
    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.yticks(yticks)
    plt.savefig(output_dir / 'x.png', **plot_dict)

    plt.figure()
    # plt.plot(n, y, 'C1')
    markerline, stemlines, baseline = plt.stem(n, y, basefmt=' ')
    plt.setp(markerline, 'color', 'C1')
    plt.setp(stemlines, 'color', 'C1')
    plt.xlabel('n')
    plt.ylabel('y[n]')
    plt.yticks(yticks)
    plt.savefig(output_dir / 'y.png', **plot_dict)
    
    c = np.correlate(x, y, 'full')
    Nc = c.shape[0] // 2
    nc = np.arange(0, c.shape[0]) - Nc

    plt.figure()
    # plt.plot(c, 'C2')
    markerline, stemlines, baseline = plt.stem(nc, c, basefmt=' ')
    plt.setp(markerline, 'color', 'C2')
    plt.setp(stemlines, 'color', 'C2')
    plt.xlabel('n')
    plt.ylabel(r'$\phi_{xy}$[n]')
    plt.savefig(output_dir / 'xy_correlation.png', **plot_dict)

    conv = np.convolve(x, y, 'full')
    plt.figure()
    markerline, stemlines, baseline = plt.stem(nc, conv, basefmt=' ')
    plt.setp(markerline, 'color', 'C4')
    plt.setp(stemlines, 'color', 'C4')
    plt.xlabel('n')
    plt.ylabel(r'$(x \ast y)$[n]')
    plt.savefig(output_dir / 'xy_convolution.png', **plot_dict)

    fig = plt.figure()
    ylim = (-8, 7)
    ax = plt.axes(xlim=(-Nc, Nc), ylim=ylim)
    visible_c = np.zeros_like(c)
    # line, = ax.plot(nc, visible_c)
    markerline, stemlines, baseline = ax.stem(nc, visible_c, basefmt=' ')
    plt.setp(markerline, 'color', 'C2')
    plt.setp(stemlines, 'color', 'C2')
    
    def update(i):
        id_1 = Nc - i
        id_2 = Nc + i
        visible_c[id_1] = c[id_1]
        visible_c[id_2] = c[id_2]
        # line.set_data(nc, visible_c)
        ax.cla()
        ax.set_ylim(ylim)
        markerline, stemlines, baseline = ax.stem(nc, visible_c, basefmt=' ')
        plt.setp(markerline, 'color', 'C2')
        plt.setp(stemlines, 'color', 'C2')

        if i == 0 or i == 1 or i == 2:
            plt.savefig(output_dir / f'correlation{i}.png', **plot_dict)

        return markerline, stemlines, baseline

    animation1 = animation.FuncAnimation(fig, update, frames=np.arange(0, Nc), interval=500, blit=True, repeat=False)
    FFwriter = animation.FFMpegWriter(fps=8)
    animation1.save(output_dir / 'correlation.mp4', writer=FFwriter)


if __name__=='__main__':
    main()
