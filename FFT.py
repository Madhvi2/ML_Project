import numpy as np


def getFFT( X, Y, Z ):

    FFTValsX = [ abs(fftval) for fftval in np.fft.fft(X) ]
    FFTValsY = [ abs(fftval) for fftval in np.fft.fft(X) ]
    FFTValsZ = [ abs(fftval) for fftval in np.fft.fft(X) ]

    FFTValsX = [ fftval**2 for fftval in FFTValsX ]
    FFTValsY = [ fftval**2 for fftval in FFTValsY ]
    FFTValsZ = [ fftval**2 for fftval in FFTValsZ ]
    
    return sum(FFTValsX)/60.0, sum(FFTValsY)/60.0, sum(FFTValsZ)/60.0
