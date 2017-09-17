import numpy as np

def testf(xmin=-5.0, xmax=5.0, dstep=0.01, noise=0.0):
    """Returns a simple sin function to test several examples
    
    Parameters:
    -----------
    xmin: Lowest x axis value
    xmax: Highest x axis value
    dstep: Step for x-axis
    noise: Amplitude of the noise to add to the signal, which is a Standard Normal distribution
    
    Returns
    -------
    x: Equally spaced x values between "xmin" and "xmax" with a step fot "dstep"
    y: The sin of x
    """
    x = np.arange(xmin, xmax, dstep)
    y = np.sin(x) + noise*np.random.randn(len(x))
    return x, y

def mov_avg(x, N=5):
    """Calculates the moving average through a simple convolution
    
    Parameters:
    -----------
    x: The data for smoothing
    N: Number of points used in the smoothing (convulution)
    
    Returns
    -------
    smt_x: x convolved with a len(N) array where every entry is 1/N    
    """
    smt_x = np.convolve(x, np.ones((N,))/N)[(N-1):] 
    return smt_x