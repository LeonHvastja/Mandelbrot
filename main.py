#main.py

"""
Project goal: make a script that generates mandelbrot set images

My monitors each have a 16:9 aspect ratio and 2560x1440 pixels.

Originally written in jupyter notebook.
"""
import numpy as np
from mandelbrot import *
from PIL import Image

# Derived from a 16:9 aspect ratio monitor
x_ratio = 16
y_ratio = 9
# dpi setting 120 is for HD, 160 is for QHD, 240 is 4k etc.
k = 160
# how many iterations to check for divergence, 70+ seems optimal
depth = 100


def main():
    x = np.linspace(-2.5, 1.5, x_ratio*k)
    y = np.linspace(-9/8, 9/8, y_ratio*k)

    points = np.asarray([complex(x_,y_) for x_ in x for y_ in y])

    # this is the cpu heavy part, might want to try using mutliple threads
    # in future versions
    points_checked = [mandelbrotCheck(z,depth,1000) for z in points]

    checked = np.asarray(points_checked)
    checked = checked.reshape(x_ratio*k,y_ratio*k)

    my_image = Image.fromarray(checked)
    name = f"Mandelbrot_{x_ratio*k}x{y_ratio*k}_depth{depth}.png"
    my_image.save(name)


if __name__ == "__main__":
    main()
