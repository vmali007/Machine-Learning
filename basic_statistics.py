import numpy as np
from scipy import stats

n = int(input("No. of valus you want you take: " ))
l = [int(i) for i in input().split()]

 
x = np.array(l)

_mean = np.mean(x)

_median = np.median(x)

_mode = stats.mode(x)

_std = x.std()

_lower = _mean - 1.96*_std/n**.5

_upper = _mean + 1.96*_std/n**.5
    
print("Mean : {}\nMedian : {}\nMode : {}\nStandard Deviation : {}\nLower and Upper Boundry : {} {}".format(_mean,_median,_mode,_std,_lower,_upper))
