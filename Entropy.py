import numpy as np


def getEntropy( X, Y, Z ):

    FFTValsX = [ abs(fftval) for fftval in np.fft.fft(X) ]
    FFTValsY = [ abs(fftval) for fftval in np.fft.fft(X) ]
    FFTValsZ = [ abs(fftval) for fftval in np.fft.fft(X) ]

    FFTValsX = [ fftval*np.log(fftval) for fftval in FFTValsX ]
    FFTValsY = [ fftval*np.log(fftval) for fftval in FFTValsY ]
    FFTValsZ = [ fftval*np.log(fftval) for fftval in FFTValsZ ]
    
    return -(sum(FFTValsX)/np.log(60.0)), -(sum(FFTValsY)/np.log(60.0)), -(sum(FFTValsZ)/np.log(60.0))
