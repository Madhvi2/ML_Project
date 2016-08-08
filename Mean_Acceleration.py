import sys,math


def mean_acc(x_window_value,y_window_value,z_window_value):
    length=len(x_window_value)
    sumx=0
    sumy=0
    sumz=0
    for j in range(0,length):
            sumx=sumx+float(x_window_value[j])
            sumy =sumy+float(y_window_value[j])
            sumz=sumz+float(z_window_value[j])
    
    mean_xacceleration=sumx/length
    mean_yacceleration=sumy/length
    mean_zacceleration=sumz/length
    return mean_xacceleration,mean_yacceleration,mean_zacceleration

def SD(x_window_value,y_window_value,z_window_value,mean_values):
        mean_xacceleration=mean_values[0]
        mean_yacceleration=mean_values[1]
        mean_zacceleration=mean_values[2]
  
        size = len(x_window_value)  
        sum_x = 0.0 
        sum_y =0.0 
        sum_z=0.0
        for n in range(0, size):  
                sum_x += math.sqrt((x_window_value[n] - mean_xacceleration)**2)
                sum_y += math.sqrt((y_window_value[n] - mean_yacceleration)**2)
                sum_z += math.sqrt((z_window_value[n] - mean_zacceleration)**2)
                  
        return math.sqrt((1.0/(size-1))*(sum_x/size)),math.sqrt((1.0/(size-1))*(sum_y/size)),math.sqrt((1.0/(size-1))*(sum_z/size))


def Variance(x_window_value,y_window_value,z_window_value,mean_values):
    mean_xacceleration=mean_values[0]
    mean_yacceleration=mean_values[1]
    mean_zacceleration=mean_values[2]
    sum_x = 0.0
    sum_y = 0.0
    sum_z = 0.0
    for value in x_window_value:
         sum_x += (value - mean_xacceleration)**2
    variance_x = sum_x/(len(x_window_value) - 1)
    for value in y_window_value:
         sum_y += (value - mean_yacceleration)**2
    variance_y = sum_y/(len(y_window_value) - 1)
    for value in z_window_value:
         sum_z += (value - mean_zacceleration)**2
    variance_z = sum_z/(len(z_window_value) - 1)

    return (variance_x,variance_y,variance_z)  
