# -*- coding: utf-8 -*-

import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np



def read_and_show(filename): # reads in image file and plots it with the grayscale value being the x axis
    im = cv2.imread(filename)
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    
    x = range(len(gray[0]))
    y = range(len(gray))
    
    x, y = np.meshgrid(x, y)
    
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    ax.contour3D(x, y, gray, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')
    
    plt.show()


#for image one
read_and_show("overhead1-image.png")
read_and_show("overhead2-image.png")
