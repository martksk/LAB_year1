import numpy as np


def Problem1(n): 
    onesk = np.ones((n,n))
    indx = [(i,j) for i in range(n-1) for j in range(n) if j > i]
    xyindx = tuple(zip(*indx))
    onesk[xyindx] = 0
    return onesk