import numpy as np
from scipy.special import comb

def binomial_pmf_cdf(n, p, k):
    """
    Compute Binomial PMF and CDF.
    """
    def combination(n, k):
        if k < 0 or k > n:
            return 0

        k = min(k, n - k)   # symmetry optimization

        result = 1
        for i in range(1, k + 1):
            result = result * (n - k + i) // i

        return result


    # Write code here
    def pmf(n, p, k):
        pmf = combination(n, k) * p**k * (1-p)**(n-k)
        return pmf 
    
    cdf = 0
    for i in range(0,k+1):
        cdf += pmf(n, p ,i)
    
    pmf = pmf(n, p ,k)


    return(pmf, cdf)