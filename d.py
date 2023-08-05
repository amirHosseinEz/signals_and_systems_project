from c import *
from a import *

h4 = 2 * np.cos(np.pi / 4 * n) * h3
h5 = 2 * np.cos(np.pi / 2 * n) * h3
h6 = 2 * np.cos(3 * np.pi / 4 * n) * h3
h7 = 2 * np.cos(np.pi * n) * h3

H4 = np.fft.fft(h4)
H5 = np.fft.fft(h5)
H6 = np.fft.fft(h6)
H7 = np.fft.fft(h7)


if __name__ == '__main__':
    plt.plot(d, np.abs(H4))
    plt.plot(d, np.abs(H5))
    plt.plot(d, np.abs(H6))
    plt.plot(d, np.abs(H7))
    plt.show()