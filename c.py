import numpy as np

from b import *

N2 = 300
N = 400
w_c = np.pi / 8
K = 1024
n = np.linspace(-N, N, K)
h3 = 0 * n
non_zero_range = (0 <= n) & (n <= 2*N2)
h3 = np.where(non_zero_range,
              np.sin(w_c * (n - N2)) / (np.pi * (n - N2)),
              0)

H3 = np.fft.fft(h3)
d = np.linspace(0,K - 1, K)
#print(d)
#print("!!!@#!@#!#@")
for i in range(0, len(d)):
    d[i] = d[i] * (np.pi * 2) / K
#print(d)
if __name__ == '__main__':
    plt.plot(d, np.abs(H3))
    plt.show()