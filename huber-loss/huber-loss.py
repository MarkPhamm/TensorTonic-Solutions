import numpy as np

def huber_loss(y_true, y_pred, delta=1.0):
    """
    Compute Huber Loss for regression.
    """
    # Write code here
    ans = 0
    if len(y_true) != len(y_pred):
        raise ValueError("mismatch")
    else: 
        for i in range(len(y_true)):
            e = y_true[i] - y_pred[i]
            if abs(e) <= delta:
                ans += (0.5 * e**2)
            else:
                ans += delta*(abs(e) - 0.5*delta)
    return ans/len(y_true)