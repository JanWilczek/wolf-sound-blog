import numpy as np
import matplotlib.pyplot as plt


def plot_signal(x, pre0=4, signal_length=6, ylabel=''):
    n = np.arange(-pre0, signal_length)
    x = np.concatenate((np.zeros((pre0,)), x, np.zeros((signal_length - x.shape[0], ))), axis=0)
    
    plt.figure()
    markerline, stemlines, baseline = plt.stem(n, x, linefmt='k-', markerfmt='ko')
    # plt.setp(baseline, 'color', '#7c7c7c')
    plt.setp(stemlines, 'linewidth', 2)
    plt.setp(baseline, 'color', 'k')
    plt.setp(baseline, 'linewidth', 0.5)
    plt.setp(baseline, 'zorder', -1)
    plt.xlabel('n')
    plt.ylabel(ylabel)
    plt.xticks(n)

def plot_circular_shift(x):
    h = np.zeros_like(x)
    h[1] = 1.0

    plot_signal(x, ylabel='x[n]')
    plot_signal(h, ylabel='h[n]')

    X = np.fft.fft(x)
    H = np.fft.fft(h)
    circular_convolution_x_h = np.real(np.fft.ifft(np.multiply(X, H)))

    plot_signal(circular_convolution_x_h, ylabel='$(x \circledast h)[n]$')

def plot_x_x_wide(x, x_wide):
    """x_wide should be 5 times longer than x"""
    n = np.arange(-2*x.shape[0], 3*x.shape[0])    
    
    plt.figure()
    baseline = plt.axhline(y=0.0, color='k', linewidth=0.5, zorder=-1)
    markerline, stemlines, _ = plt.stem(n[2*x.shape[0]:3*x.shape[0]], x, linefmt='k-', markerfmt='ko', basefmt=' ')
    plt.setp(stemlines, 'linewidth', 2)
    pre_length = x.shape[0] + 3
    markerline, stemlines, _ = plt.stem(n[2*x.shape[0]-pre_length:2*x.shape[0]], x_wide[2*x.shape[0]-pre_length:2*x.shape[0]], basefmt=' ')
    plt.setp(markerline, 'color', '#7c7c7c')
    plt.setp(stemlines, 'color', '#7c7c7c')
    post_length = x.shape[0] + 2
    markerline, stemlines, _ = plt.stem(n[3*x.shape[0]:3*x.shape[0]+post_length], x_wide[x.shape[0]:x.shape[0]+post_length], basefmt=' ')
    plt.setp(markerline, 'color', '#7c7c7c')
    plt.setp(stemlines, 'color', '#7c7c7c')

    plt.xlabel('n')
    plt.ylabel('x[n]')
    plt.xticks(n)

def plot_repeated_signal(x):
    x_repeated = np.tile(x, 5)
    x_wide = np.zeros((x_repeated.shape[0],))

    plot_x_x_wide(x, x_wide)
    plot_x_x_wide(x, x_repeated)
    

def main():
    x = np.array([1., 0.7, 0.3, 0.1])
    plot_circular_shift(x)
    plot_repeated_signal(x)

    plt.show()


if __name__ == '__main__':
    main()
