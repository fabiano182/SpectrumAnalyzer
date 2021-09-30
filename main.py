import numpy as np
import matplotlib.pyplot as plt

class SpectrumAnalyzer:

    def __init__(self, signal, fs):
        self.signal = signal
        self.fs = fs

    def plot(self):
        x = self.signal
        y = np.linspace(0, x.size/self.fs, x.size)


        plt.plot(y,x)
        plt.show()
    
    def fft(self):
        x = self.signal

        amp = np.fft.fft(x)
        freq = np.fft.fftfreq(x.size)*self.fs

        plt.plot(amp)
        plt.show()

if __name__ == '__main__':

    #Sin 10Hz with frequency sample of 1kHz
    f = 10
    T = 10
    fs = 1000
    Ts = 1./fs
    N = int(T/Ts)

    t = np.linspace(0, T, N)
    signal = np.sin(2*np.pi*f*t)

    Signal = SpectrumAnalyzer(signal, fs)
    Signal.fft()