#mandelbrot.py
import numpy as np

def rec(z, c):
    return np.square(z) + c

def divergence_check(points, divergence, iteration):
    diverge_indicator = np.where(np.absolute(points) > 1000, 1, 0)
    not_diverge = (diverge_indicator - 1)*(-1)
    
    
    return (points*not_diverge, divergence + diverge_indicator*iteration)
