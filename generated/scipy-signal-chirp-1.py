# The following will be used in the examples:

from scipy.signal import chirp, spectrogram
import matplotlib.pyplot as plt

# For the first example, we'll plot the waveform for a linear chirp
# from 6 Hz to 1 Hz over 10 seconds:

t = np.linspace(0, 10, 5001)
w = chirp(t, f0=6, f1=1, t1=10, method='linear')
plt.plot(t, w)
plt.title("Linear Chirp, f(0)=6, f(10)=1")
plt.xlabel('t (sec)')
plt.show()

# For the remaining examples, we'll use higher frequency ranges,
# and demonstrate the result using `scipy.signal.spectrogram`.
# We'll use a 10 second interval sampled at 8000 Hz.

fs = 8000
T = 10
t = np.linspace(0, T, T*fs, endpoint=False)

# Quadratic chirp from 1500 Hz to 250 Hz over 10 seconds
# (vertex of the parabolic curve of the frequency is at t=0):

w = chirp(t, f0=1500, f1=250, t1=10, method='quadratic')
ff, tt, Sxx = spectrogram(w, fs=fs, noverlap=256, nperseg=512,
                          nfft=2048)
plt.pcolormesh(tt, ff[:513], Sxx[:513], cmap='gray_r')
plt.title('Quadratic Chirp, f(0)=1500, f(10)=250')
plt.xlabel('t (sec)')
plt.ylabel('Frequency (Hz)')
plt.grid()
plt.show()

# Quadratic chirp from 1500 Hz to 250 Hz over 10 seconds
# (vertex of the parabolic curve of the frequency is at t=10):

w = chirp(t, f0=1500, f1=250, t1=10, method='quadratic',
          vertex_zero=False)
ff, tt, Sxx = spectrogram(w, fs=fs, noverlap=256, nperseg=512,
                          nfft=2048)
plt.pcolormesh(tt, ff[:513], Sxx[:513], cmap='gray_r')
plt.title('Quadratic Chirp, f(0)=1500, f(10)=250\n' +
          '(vertex_zero=False)')
plt.xlabel('t (sec)')
plt.ylabel('Frequency (Hz)')
plt.grid()
plt.show()

# Logarithmic chirp from 1500 Hz to 250 Hz over 10 seconds:

w = chirp(t, f0=1500, f1=250, t1=10, method='logarithmic')
ff, tt, Sxx = spectrogram(w, fs=fs, noverlap=256, nperseg=512,
                          nfft=2048)
plt.pcolormesh(tt, ff[:513], Sxx[:513], cmap='gray_r')
plt.title('Logarithmic Chirp, f(0)=1500, f(10)=250')
plt.xlabel('t (sec)')
plt.ylabel('Frequency (Hz)')
plt.grid()
plt.show()

# Hyperbolic chirp from 1500 Hz to 250 Hz over 10 seconds:

w = chirp(t, f0=1500, f1=250, t1=10, method='hyperbolic')
ff, tt, Sxx = spectrogram(w, fs=fs, noverlap=256, nperseg=512,
                          nfft=2048)
plt.pcolormesh(tt, ff[:513], Sxx[:513], cmap='gray_r')
plt.title('Hyperbolic Chirp, f(0)=1500, f(10)=250')
plt.xlabel('t (sec)')
plt.ylabel('Frequency (Hz)')
plt.grid()
plt.show()
