def percent_change(series):
    """
    Compute the fractional change between consecutive values.
    """
    # Write code here
    n = len(series)
    ans = []
    for i in range(1,n):
        if series[i-1] == 0:
            ans.append(0)
        else:
            ans.append((series[i] - series[i-1])/series[i-1])
    return ans
