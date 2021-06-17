import numpy as np
from matplotlib import pyplot as plt


def main():
    rg = np.random.default_rng()
    shape = (100000,)
    x = rg.uniform(-1.0, 1.0, shape)
    y = rg.uniform(-1.0, 1.0, shape)

    correlation_from_convolution = np.flip(np.convolve(np.flip(x), y, 'full'))
    correlation = np.correlate(x, y, 'full')

    np.testing.assert_array_almost_equal(
        correlation_from_convolution, correlation, decimal=10)

if __name__=='__main__':
    main()
