import numpy as np


def naive_convolution(x, h):    
    """Compute the discrete convolution of two sequences"""
    
    # Make x correspond to the longer signal
    if len(x) < len(h):
        x, h = h, x
        
    M = len(x)
    N = len(h)
    
    # Convenience transformations
    x = pad_zeros_to(x, M+2*(N-1))
    x = np.roll(x, N-1)
    
    h = np.flip(h)
    
    y = np.zeros(M+N-1)

    # Delay h and calculate the inner product with the 
    # corresponding samples in x
    for i in range(len(y)):
        y[i] = x[i:i+N].dot(h)
        
    return y

def next_power_of_2(n):
    return 1 << (int(np.log2(n - 1)) + 1)

def pad_zeros_to(x, new_length):
    """Append new_length - x.shape[0] zeros to x's end via copy."""
    output = np.zeros((new_length,))
    output[:x.shape[0]] = x
    return output

def fft_convolution(x, h, K=None):
    Nx = x.shape[0]
    Nh = h.shape[0]
    Ny = Nx + Nh - 1 # output length

    # Make K smallest optimal
    if K is None:
        K = next_power_of_2(Ny)

    # Calculate the fast Fourier transforms 
    # of the time-domain signals
    X = np.fft.fft(pad_zeros_to(x, K))
    H = np.fft.fft(pad_zeros_to(h, K))

    # Perform circular convolution in the frequency domain
    Y = np.multiply(X, H)

    # Go back to time domain
    y = np.real(np.fft.ifft(Y))

    # Trim the signal to the expected length
    return y[:Ny]

def overlap_add_convolution(x, h, B, K=None):
    """Overlap-Add convolution of x and h with block length B"""

    M = len(x)
    N = len(h)

    # Calculate the number of input blocks
    num_input_blocks = np.ceil(M / B).astype(int)

    # Pad x to an integer multiple of B
    xp = pad_zeros_to(x, num_input_blocks*B)

    # Your turn ...
    output_size = num_input_blocks * B + N - 1
    y = np.zeros((output_size,))
    
    # Convolve all blocks
    for n in range(num_input_blocks):
        # Extract the n-th input block
        xb = xp[n*B:(n+1)*B]

        # Fast convolution
        u = fft_convolution(xb, h, K)

        # Overlap-Add the partial convolution result
        y[n*B:n*B+len(u)] += u

    return y[:M+N-1]

def overlap_save_convolution(x, h, B, K=None):
    """Overlap-Save convolution of x and h with block length B"""

    M = len(x)
    N = len(h)

    if K is None:
        K = max(B, next_power_of_2(N))
        
    # Calculate the number of input blocks
    num_input_blocks = np.ceil(M / B).astype(int) \
                     + np.ceil(K / B).astype(int) - 1

    # Pad x to an integer multiple of B
    xp = pad_zeros_to(x, num_input_blocks*B)

    output_size = num_input_blocks * B + N - 1
    y = np.zeros((output_size,))
    
    # Input buffer
    xw = np.zeros((K,))

    # Convolve all blocks
    for n in range(num_input_blocks):
        # Extract the n-th input block
        xb = xp[n*B:n*B+B]

        # Sliding window of the input
        xw = np.roll(xw, -B)
        xw[-B:] = xb

        # Fast convolution
        u = fft_convolution(xw, h, K)

        # Save the valid output samples
        y[n*B:n*B+B] = u[-B:]

    return y[:M+N-1]

def main():
    pass

if __name__ == '__main__':
    main()
