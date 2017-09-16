import numpy as np

def testf(xmin=-5.0, xmax=5.0, dstep=0.01):
    """Returns a simple sin function to be used in several examples
    
    Parameters:
    -----------
    xmin: Lowest x axis value
    xmax: Highest x axis value
    dstep: Step for x-axis
    
    Returns
    -------
    x: Equally spaced x values between "xmin" and "xmax" with a step fot "dstep"
    y: The sin of x
    """
    x = np.arange(xmin, xmax, dstep)
    y = np.sin(x)
    return x, y