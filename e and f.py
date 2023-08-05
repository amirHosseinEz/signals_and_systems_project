import soundfile as sf
import numpy as np

from d import h3, h4, h5, h6

# print("HERE from E")
# print(h3)
# h9 = h3 * 3
# print(h9)
# print("ASDASDASDASDASD")

data, samplerate = sf.read('signal_chlorine.wav')
dataL = []
dataR = []
for i in data:
    dataL.append(i[0])
    dataR.append(i[1])

print(data, samplerate)
print(h3)
convolvedLh3 = np.convolve(h3, dataL)
convolvedRh3 = np.convolve(h3, dataR)
finalh3 = []

for i in range(0, len(convolvedRh3)):
    finalh3.append([convolvedLh3[i], convolvedRh3[i]])

sf.write('final3.wav', finalh3, samplerate)

convolvedLh4 = np.convolve(h4, dataL)
convolvedRh4 = np.convolve(h4, dataR)
finalh4 = []

for i in range(0, len(convolvedRh4)):
    finalh4.append([convolvedLh4[i], convolvedRh4[i]])

sf.write('final4.wav', finalh4, samplerate)

convolvedLh5 = np.convolve(h5, dataL)
convolvedRh5 = np.convolve(h5, dataR)
finalh5 = []

for i in range(0, len(convolvedRh5)):
    finalh5.append([convolvedLh5[i], convolvedRh5[i]])

sf.write('final5.wav', finalh5, samplerate)

h8 = h3*3 + h4 + (1/3)*h5
# print("h8 ==== ")
# print(h8)

convolvedLh8 = np.convolve(h5, dataL)
convolvedRh8 = np.convolve(h5, dataR)
finalh8 = []

for i in range(0, len(convolvedRh8)):
    finalh8.append([convolvedLh5[i], convolvedRh8[i]])

sf.write('final8.wav', finalh8, samplerate)


h8 = h3*(1/3) + h4 + 3*h5
# print("h9 ==== ")
# print(h9)

convolvedLh9 = np.convolve(h9, dataL)
convolvedRh9 = np.convolve(h9, dataR)
finalh9 = []

for i in range(0, len(convolvedRh9)):
    finalh9.append([convolvedLh9[i], convolvedRh9[i]])

sf.write('final9.wav', finalh9, samplerate)