from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from example1 import savefig, plot_x_x_wide


def periodic_convolution_naive(x, h):
    assert x.shape == h.shape, 'Inputs to periodic convolution must be of the same period, i.e., shape.'

    output = np.zeros_like(x)
    N = x.shape[0]

    for n in range(N):
        for m in range(N):
            output[n] += x[m] * h[(n - m) % N]
    
    return output

def periodic_convolution_fast(x, h):
    X = np.fft.fft(x)
    H = np.fft.fft(H)
    return np.real(np.fft.ifft(np.multiply(X, H)))

def plot_periodic_convolution(x, h):
    tile_count = 5
    x_repeated = np.tile(x, tile_count)
    h_repeated = np.tile(h, tile_count)

    # periodic_convolution_x_h = np.convolve(x_repeated, h_repeated, 'same')
    periodic_convolution_x_h = periodic_convolution_naive(x, h)
    periodic_convolution_x_h_tiled = np.tile(periodic_convolution_x_h, tile_count)    

    plot_x_x_wide(x, x_repeated, xlabel='n', ylabel='x[n]')
    plot_x_x_wide(h, h_repeated, xlabel='n', ylabel='h[n]')
    plot_x_x_wide(periodic_convolution_x_h, periodic_convolution_x_h_tiled, xlabel='n', ylabel='$(x \circledast h)[n]$')

def main():
    x = np.array([1., 0.7, 0.3, 0.1])
    h = np.zeros_like(x)
    h[1] = 1.0
    
    plot_periodic_convolution(x, h)
    plt.show()


if __name__ == '__main__':
    main()