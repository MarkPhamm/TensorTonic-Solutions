import math 
def elu(x, alpha):
    """
    Apply ELU activation to each element.
    """
    # Write code here
    ans = []
    for var in x:
        if var > 0:
            ans.append(var)
        else:
            ans.append(alpha*(math.e**var - 1))
    return ans 