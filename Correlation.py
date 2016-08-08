from numpy import array, mean, std
from scipy.spatial.distance import correlation


def GetCorr( XAxis, YAxis, ZAxis ):

    X = array(XAxis)
    Y = array(YAxis)
    Z = array(ZAxis)
    
    #Normalize
    X_A = (X - mean(X)) / (std(X) * len(X))
    Y_A = (Y - mean(Y)) /  std(Y)
    CorrA = 1.0-correlation(X_A, Y_A)

    Y_B = (Y - mean(Y)) / (std(Y) * len(Y))
    Z_B = (Z - mean(Z)) /  std(Z)
    CorrB = 1.0-correlation(Y_B, Z_B)

    Z_C = (Z - mean(Z)) / (std(Z) * len(Z))
    X_C = (X - mean(X)) /  std(X)
    CorrC = 1.0-correlation(Z_C, X_C)
    
    return CorrA, CorrB, CorrC


if __name__ == "__main__":
    print GetCorr( [1.0,2.0,3.0] , [3.0,2.0,1.0] , [2.0,3.0,1.0] )

