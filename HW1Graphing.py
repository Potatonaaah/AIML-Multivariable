from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import matplotlib.pyplot as plt
import numpy as np

def zFunction(x, y):
    z = 1-((np.power(x, 2))/4) - (np.power(y, 2)/9)
    return np.sqrt(z)

plt.show()
    
    
x = np.linspace(-2, 2, 20)
y = np.linspace(-3, 3, 40)

x, y = np.meshgrid(x, y)

z = zFunction(x, y)

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(x, y, z, color='green')
ax.plot_wireframe(x, y, -1*z, color='green')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
