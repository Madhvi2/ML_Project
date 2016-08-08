import os
import struct
import datetime

def DECODE( File ):

    FILENAME = os.path.splitext(File)[0]

    FileHandle = open( File , "rb" )
    Data = FileHandle.read(8)

    TxtFile = open( FILENAME+"_txt.txt" , "w" )

    while Data != '':

        Time = struct.unpack( '>q' , Data )[0]
        Data = FileHandle.read(4)
        X = struct.unpack( '>f' , Data )[0]
        Data = FileHandle.read(4)
        Y = struct.unpack( '>f' , Data )[0]
        Data = FileHandle.read(4)
        Z = struct.unpack( '>f' , Data )[0]
        Data = FileHandle.read(8)
 
        TxtFile.write( str(Time)+","+str(X)+","+str(Y)+","+str(Z)+"\n" )

    FileHandle.close()
    TxtFile.close()


if __name__ == "__main__":

    try:
        import sys
        DECODE(sys.argv[1])

    except:
        print "Usage: *.py [FilePath]"
        print "Output File: [OriginalFileName]_txt.txt"
