from a import *

h2 = h1 * np.exp(1j * np.pi * n)
H2 = np.fft.fft(h2)

if __name__ == '__main__':
	plt.plot(d, np.abs(H2))
	plt.show()