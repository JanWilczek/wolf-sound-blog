import numpy as np
from matplotlib import pyplot as plt


def main():
    rg = np.random.default_rng()
    shape = (44100,)
    x = rg.normal(-1.0, 1.0, shape)
    y = rg.normal(-1.0, 1.0, shape)

    convolution = np.convolve(x, y, 'full')
    correlation = np.flip(np.correlate(np.flip(x), y, 'full'))

    np.testing.assert_array_almost_equal(convolution, correlation, decimal=10)

if __name__=='__main__':
    main()
