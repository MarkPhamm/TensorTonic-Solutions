import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    # Write code here
    ans = 0
    total = 0

    n = len(x)
    for i in range(n):
        ans += x[i] * p[i]
        total += p[i]
    
    if total != 1:
        raise ValueError("total p != 1")
        

    return ans 
