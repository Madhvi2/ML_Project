from scipy.signal.filter_design import *
from scipy.signal import lfilter

import os
import struct
import datetime

import PC


def Strip( Start , End , AcclX , TimeData ):

    AcclXTemp = []
    TimeDataTemp = []
    counter = 0
    for time in TimeData:
        counter += 1
        if( time >= Start and time <= End ):
            TimeDataTemp.append( time )
            AcclXTemp.append( AcclX[counter] )


    return AcclXTemp, TimeDataTemp


def DECODE( File , Axis , Start , End ):

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

    START = int(Start)
    END = int(End)
    
    AcclX, TimeData = Strip(START,END,AcclX,TimeData)
    AcclY, TimeData = Strip(START,END,AcclY,TimeData)
    AcclZ, TimeData = Strip(START,END,AcclZ,TimeData)

    if( Axis == 'x' ): return AcclX, TimeData
    if( Axis == 'y' ): return AcclY, TimeData
    if( Axis == 'z' ): return AcclZ, TimeData
    


if __name__ == "__main__":

    try:
        import sys
        if( sys.argv[2] == 'A' ):
            File = "Accelerometer.acl"
        else: "Orientation.orn"
        
        DECODE( os.path.join( sys.argv[1] , "Accelerometer.acl" ) , sys.argv[3] , sys.argv[4], sys.argv[5] )

    except:
        print "Usage: *.py [Sample #] [A/B] [x|y|z] [Start] [End]"
        print "[A/B]: Accelerometer / Orientation"
        print "[x|y|z]: Axis"
