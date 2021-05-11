import numpy as np


def naive_convolution(x, h):
    Nx = x.shape[0]
    Nh = h.shape[0]
    Ny = Nx + Nh - 1
    
    # Allocate the output buffer
    y = np.zeros((Ny,))

    h_flipped = np.flip(h)

    for n in range(Ny):
        # overlap_length = 

        y[n] = np.dot()

def next_power_of_2(n):
    return 1 << (int(np.log2(n - 1)) + 1)

def pad_zeros_to(x, new_length):
    """Append new_length - x.shape[0] zeros to x's end via copy."""
    output = np.zeros((new_length,))
    output[:x.shape[0]] = x
    return output

def fft_convolution(x, h):
    Nx = x.shape[0]
    Nh = h.shape[0]
    Ny = Nx + Nh - 1

    K = next_power_of_2(Ny)

    X = np.fft.fft(pad_zeros_to(x, K))
    H = np.fft.fft(pad_zeros_to(h, K))

    Y = np.multiply(X, H)

    y = np.real(np.ifft(Y))

    return y[:Ny]


def main():
    pass

if __name__ == '__main__':
    main()
