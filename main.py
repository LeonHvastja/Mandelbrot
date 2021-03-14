#main.py

"""
Project goal: make a script that generates mandelbrot set images

Goals:
1.Make code that uses the math to generate a single point value
...
2.Generate a set of complex numbers to run through the calculations
The mandelbrot set occurs roughly from x = [-2,0.5] and y = [-1, 1] so it
would make sense to bound the values to roughly that range.

My monitors each have a 16:9 aspect ratio and 2560x1440 pixels.
"""
import numpy as np


def check(c_number):
    """
    The return value of this function tells us if the point is
    cointained in the mandelbrot set.
    """
    z = 0
    for i in range(1000):
        z = f_c(z, c_number)
        #the 1000*c_number is an arbitrary limit i made up, seems to work
        if(abs(z) > 1000*abs(c_number)):
            print("This number diverges")
            return False
    print("This number does not diverge")
    return True

def calculate(c_number, iterations):
    z = 0
    for i in range(iterations):
        z = f_c(z,c_number)
    return z

def f_c(z,c_number):
    return z**2 + c_number

# this function should return a list of complex numbers to run through
# based on something like pixel count or similar
def numbers(x_aspect, y_aspect, k):
    """
    k is the factor we multiply the two aspect ratios to get total pixel
    count, it thus serves as a sort of scaling factor
    the native k for my monitors is 160
    """
    lower_x_bound = -2.5
    upper_x_bound = 1.5
    lower_y_bound = -9/8
    upper_y_bound = 9/8
    # the multiplication by 4 is to convert x and y coordinates
    # to aspect ratio "units"
    x_resolution = x_aspect*k
    y_resolution = y_aspect*k
    x_values = np.linspace(lower_x_bound, upper_x_bound, x_resolution)
    y_values = np.linspace(lower_y_bound, upper_y_bound, y_resolution)
    #list comprehension to generate all of our points
    all_values =  [complex(x,y) for x in x_values for y in y_values]
