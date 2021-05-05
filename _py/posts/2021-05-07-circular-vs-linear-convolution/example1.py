import numpy as np
import matplotlib.pyplot as plt


def plot_signal(x, pre0=4, signal_length=6, ylabel=''):
    n = np.arange(-pre0, signal_length)
    x = np.concatenate((np.zeros((pre0,)), x, np.zeros((signal_length - x.shape[0], ))), axis=0)
    
    plt.figure()
    _, _, baseline = plt.stem(n, x, linefmt='k-', markerfmt='ko')
    plt.setp(baseline, 'color', '#AcAcAc')
    plt.setp(baseline, 'zorder', -1)
    plt.xlabel('n')
    plt.ylabel(ylabel)
    plt.xticks(n)


def main():
    x = np.array([1., 0.7, 0.3, 0.1])
    h = np.array([0., 1., 0., 0.])

    plot_signal(x, ylabel='x[n]')
    plot_signal(h, ylabel='h[n]')

    X = np.fft.fft(x)
    H = np.fft.fft(h)
    circular_convolution_x_h = np.real(np.fft.ifft(np.multiply(X, H)))

    plot_signal(circular_convolution_x_h, ylabel='$(x \circledast h)[n]$')

    plt.show()


if __name__ == '__main__':
    main()
