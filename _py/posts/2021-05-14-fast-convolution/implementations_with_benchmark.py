import numpy as np


def naive_convolution(x, h):
    Nx = x.shape[0]
    Nh = h.shape[0]
    Ny = Nx + Nh - 1
    
    # Allocate the output buffer
    y = np.zeros((Ny,))

    h_flipped = np.flip(h)

    for n in range(Ny):
        overlap_length = 

        y[n] = np.dot()

def main():


if __name__ == '__main__':
    main()
