# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 22:11:33 2020

@author: Paul Hao
"""


import cv2
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

image = cv2.imread("overhead2-image.png")
blue = image[:,:,0]
green= image[:,:,1]
red= image[:,:,2]




x = range(len(image[0]))
y = range(len(image))

x, y = np.meshgrid(x, y)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(x, y, blue, color='blue')
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(x, y, green, color='green')
fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(x, y, red, color='red')


    

