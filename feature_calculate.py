import os, glob
from Mean_Acceleration import *
from Correlation import *
from Entropy import *
from FFT import *
import math

path = raw_input("Enter the path:")
window_size=60
def Normalise(AcclX):
    Max = 0.0
    for val in AcclX:
       val = float(val)
       if abs(val) > Max:
           Max = abs(val)       
    AcclX = [ float(val)/float(Max) for val in AcclX ]
    return AcclX
for infile in glob.glob( os.path.join(path, '*.txt') ):
        print("current file is: " + infile)
        temp = infile.split("/")
        length=len(temp)
        label = temp[length-1].split(".")[0].split("_")[1][0]
        fin=open(infile,"r")
        content= fin.read()
        fin.close()
        content=content[:-1]
        content=content.split("\n")
        xvalue=[]
        yvalue=[]
        zvalue=[]
        for line in content:
            xvalue.append(line.split(",")[1])
            yvalue.append(line.split(",")[2])
            zvalue.append(line.split(",")[3])
        xvalue=Normalise(xvalue)
        yvalue=Normalise(yvalue)
        zvalue=Normalise(zvalue)
            
        count=1
        value=len(xvalue)/window_size
        for i in range(value):
            x_window_value=[]
            y_window_value=[]
            z_window_value=[]
            for j in range(0,window_size):
                x_window_value.append(float(xvalue[count+j-1]))
                y_window_value.append(float(yvalue[count+j-1]))
                z_window_value.append(float(zvalue[count+j-1]))
            mean_values=mean_acc(x_window_value,y_window_value,z_window_value)
            std_deviation_values=SD(x_window_value,y_window_value,z_window_value,mean_values)
            Corelation_values =GetCorr(x_window_value,y_window_value,z_window_value)
            Variance_values=Variance(x_window_value,y_window_value,z_window_value,mean_values)
            entropy_values=getEntropy(x_window_value,y_window_value,z_window_value)
            FFT_values=getFFT(x_window_value,y_window_value,z_window_value)
            f=open(path+"/feature_set.txt","a")
            for i in range(len(mean_values)):
                f.write(str(mean_values[i])+",")
            for j in range(len(Corelation_values)):
                f.write(str(Corelation_values[j]))
                f.write(",")        
            for k in range(len(std_deviation_values)):
                f.write(str(std_deviation_values[k]))
                f.write(",")
            for l in range(len(Variance_values)):
                f.write(str(Variance_values[l]))
                f.write(",")
            """for m in range(len(entropy_values)):
                f.write(str(entropy_values[m]))
                f.write(",")
            for n in range(len(FFT_values)):
                f.write(str(FFT_values[n]))
                f.write(",")"""
            f.write(label+"\n")
            
            count=count+window_size