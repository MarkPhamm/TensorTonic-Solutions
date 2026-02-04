def exponential_moving_average(values, alpha):
    """
    Compute the exponential moving average of the given values.
    """
    ans = []

    ans.append(values[0])

    for i in range(1,len(values)):
        ans.append(alpha*values[i] + (1-alpha)*ans[i-1])
    
    return ans