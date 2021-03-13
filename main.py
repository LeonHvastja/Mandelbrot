#main.py

"""
Project goal: make a script that generates mandelbrot set images

Goals:
1.Make code that uses the math to generate a single point value
...
2.Generate a set of complex numbers to run through the calculations
"""

def check(c_number):
    z = 0
    for i in range(1000):
        z = f_c(z, c_number)
        #the 1000*c_number is an arbitrary limit i made up, seems to work
        if(abs(z) > 1000*abs(c_number)):
            print("This number diverges")
            return
    print("This number does not diverge")

def calculate(c_number, iterations):
    z = 0
    for i in range(iterations):
        z = f_c(z,c_number)
    return z

def f_c(z,c_number):
    return z**2 + c
