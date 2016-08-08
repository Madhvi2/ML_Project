from pylab import *
import scipy.interpolate


def Interpolate( data_x , data_y ):

    print data_x, data_y

    spl = scipy.interpolate.splrep(data_x, data_y)
    figure(1, figsize=(6.0,4.0), dpi=100)

    FREQ = 1/100.0
    x = arange( 0.0, data_x[-1], FREQ)
    y = scipy.interpolate.splev( x, spl)
    plot( x, y, "bo" )
    
    plot( data_x, data_y, "rs" )
    title( 'scipy spline interpolation' )
    show()

    return x,y
