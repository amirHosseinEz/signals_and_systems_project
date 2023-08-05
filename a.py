import numpy as np
import matplotlib.pyplot as plt

N1 = 4
N = 400
K = 1024
n = np.linspace(-N, N, K)
d = np.linspace(0,K - 1, K)
#print(d)
one_range = (0 <= n) & (n <= 2*N1)

h1 = np.where(one_range, 1, 0)

freq = np.fft.fftfreq(n.shape[-1])

#print(freq)
H1 = np.fft.fft(h1)

if __name__ == '__main__':
	plt.plot(d, np.abs(H1))
	plt.show()