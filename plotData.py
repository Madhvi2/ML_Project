from pylab import *

import matplotlib.pyplot as Graph
import matplotlib.mlab as MathLab
import matplotlib as MT

import os
import struct
import datetime

def DECODE( File , Axis, render ):

    Extension = os.path.splitext(File)

    FileHandle = open( File , "rb" )
    Data = FileHandle.read(8)

    TimeData = []
    AcclX = []
    AcclY = []
    AcclZ = []
    
    while Data != '':

        Time = struct.unpack( '>q' , Data )
        #TimeData.append( datetime.datetime.fromtimestamp(Time[0]/1000) )
        TimeData.append( Time[0] )
        #print datetime.datetime.fromtimestamp(Time[0]/1000)
        Data = FileHandle.read(4)
        AcclX.append( struct.unpack( '>f' , Data )[0] )
        #print struct.unpack( '>f' , Data )[0]
        Data = FileHandle.read(4)
        AcclY.append( struct.unpack( '>f' , Data )[0] )
        #print struct.unpack( '>f' , Data )[0]
        Data = FileHandle.read(4)
        AcclZ.append( struct.unpack( '>f' , Data )[0] )
        #print struct.unpack( '>f' , Data )[0]
        Data = FileHandle.read(8)
    
    TimeZero = TimeData[0]
    TimeData = [ val-TimeZero for val in TimeData ]
    TimeData = [ float(val)/1000.0 for val in TimeData ]
    """
    Graph.grid( True )
    Graph.title( "Stairs and Walking Combined" )
    MT.rcParams.update({'font.size': 28})
    """

    
    if( 'x' in Axis ):
        if( render == 's' ): subplot(311)
        Graph.plot( TimeData , AcclX , "r-" )
        Graph.plot( TimeData , AcclX , "go" )
        #Graph.yticks( [-10,0,10,20] )
        #Graph.xlim(30,40)
    if( 'y' in Axis ):
        if( render == 's' ): subplot(312)
        Graph.plot( TimeData , AcclY , "g-" )
        Graph.plot( TimeData , AcclY , "ro" )
        #Graph.yticks( [-20,-10,0,10] )
        #Graph.xlim(30,40)
    if( 'z' in Axis ):
        if( render == 's' ): subplot(313)
        Graph.plot( TimeData , AcclZ , "y-" )
        Graph.plot( TimeData , AcclZ , "go" )
        #Graph.yticks( [-15,-5,5,15] )
        #Graph.xlim(30,40)

    Graph.grid( True )
    Graph.show()


if __name__ == "__main__":

    try:
        import sys
        if( sys.argv[2] == 'A' ):
            File = "Accelerometer.acl"
        else: "Orientation.orn"
        
        DECODE( os.path.join( sys.argv[1] , "Accelerometer.acl" ) , sys.argv[3] , sys.argv[4] )

    except:
        print "Usage: *.py [Sample #] [A/B] [x|y|z] [s/o]"
        print "[A/B]: Accelerometer / Orientation"
        print "[x|y|z]: Axis"
        print "[s/o]: Subplot/Overlay"
