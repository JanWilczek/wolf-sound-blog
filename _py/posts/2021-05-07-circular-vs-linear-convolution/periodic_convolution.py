from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from example1 import savefig, plot_x_x_wide


def periodic_convolution_at(x, h, n):
    assert x.shape == h.shape, 'Inputs to periodic convolution must be of the same period, i.e., shape.'
    
    N = x.shape[0]

    output = 0.0
    for m in range(N):
            output += x[m % N] * h[(n - m) % N]
    return output

def periodic_convolution_naive(x, h):
    assert x.shape == h.shape, 'Inputs to periodic convolution '\
                               'must be of the same period, i.e., shape.'

    output = np.zeros_like(x)
    N = x.shape[0]

    for n in range(N):
        output[n] = periodic_convolution_at(x, h, n)
    
    return output

def periodic_convolution_fast(x, h):
    X = np.fft.fft(x)
    H = np.fft.fft(h)
    return np.real(np.fft.ifft(np.multiply(X, H)))

def plot_periodic_convolution(x, h):
    tile_count = 5
    x_repeated = np.tile(x, tile_count)
    h_repeated = np.tile(h, tile_count)

    periodic_convolution_x_h = periodic_convolution_naive(x, h)
    periodic_convolution_x_h = periodic_convolution_fast(x, h)
    periodic_convolution_x_h_full = np.zeros(tile_count * x.shape[0])
    runs_before_0 = 2
    for n in range(-runs_before_0*x.shape[0], (tile_count - runs_before_0)*x.shape[0]):
        periodic_convolution_x_h_full[n] = periodic_convolution_at(x, h, n)

    plot_x_x_wide(x, x_repeated, xlabel='n', ylabel='$\\tilde{x}[n]$')
    savefig('x_tilde_repeated')
    plot_x_x_wide(h, h_repeated, xlabel='n', ylabel='$\\tilde{h}[n]$')
    plot_x_x_wide(periodic_convolution_x_h, periodic_convolution_x_h_full, xlabel='n', ylabel='$(x \circledast h)[n]$')
    savefig('periodic_convolution')

    linear_convolution_x_h = np.convolve(x, h[:2], 'full')
    linear_convolution_full = np.zeros_like(h_repeated)
    plot_x_x_wide(linear_convolution_x_h, linear_convolution_full, xlabel='n', ylabel='$(x \\ast h)[n]$')
    savefig('linear_convolution_full')

def main():
    x = np.array([1., 0.7, 0.3, 0.1])
    h = np.zeros_like(x)
    h[1] = 1.0
    
    plot_periodic_convolution(x, h)
    # plt.show()


if __name__ == '__main__':
    main()