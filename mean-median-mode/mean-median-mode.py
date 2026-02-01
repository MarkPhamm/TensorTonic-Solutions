import numpy as np
from collections import Counter
import math 

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    n = len(x)
    d = {}
    total = 0
    ## Mean 
    for i in range(n):
        total += x[i]
        d[x[i]] = d.get(x[i], 0) + 1
    
    mean = total/n 

    ## Median 
    if n % 2 == 1:
        median = x[n // 2]
    else:
        median = (x[n // 2 - 1] + x[n // 2]) / 2
    
    # Mode
    sorted_d = sorted(d.items(), key=lambda item: item[1], reverse = True)
    mode = sorted_d[0][0]
    
    return  (mean, median, mode)