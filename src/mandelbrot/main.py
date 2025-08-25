#main.py

"""
Project goal: make a script that generates mandelbrot set images.
"""

import numpy as np
from mandelbrot import *
from PIL import Image
from matplotlib import cm

# Derived from a 16:9 aspect ratio monitor
x_ratio = 16
y_ratio = 9
# dpi setting 120 is for HD, 160 is for QHD, 240 is 4k etc.
k = int(input("Choose resolution factor. For reference 120 for HD, 160 for QHD, 240 for 4K, or other:"))


def main():
    # how many iterations to check for divergence, 70+ gives good results
    depth = int(input("Choose desired number of iterations:"))

    x = np.linspace(-2.5, 1.5, x_ratio*k)
    y = np.linspace(-9/8, 9/8, y_ratio*k)
    shape_tuple = (len(x),len(y))

    # initialize point array
    points = np.reshape([complex(x_,y_) for x_ in x for y_ in y], shape_tuple)
    points = points.astype(np.csingle)

    # initialize divergence array
    divergence = np.full(shape_tuple, 0)
    z = np.full(shape_tuple,0)

    for i in range(depth):
        z = rec(z, points)
        z, divergence = divergence_check(z, divergence, i)

    my_image = Image.fromarray(np.uint8(cm.bone_r(divergence.T)*255))
    name = f"Mandelbrot_{x_ratio*k}x{y_ratio*k}_depth_{depth}.png"
    my_image.save(name)


if __name__ == "__main__":
    main()
