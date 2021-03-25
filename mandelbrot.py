#mandelbrot.py

def rec(c, z):
    return z**2 + c

def mandelbrotCheck(c, depth = 100, threshold = 1000):
    z = 0
    for i in range(depth):
        z = rec(z, c)
        if(abs(z) > 1000*abs(c)):
            return False
    return True
