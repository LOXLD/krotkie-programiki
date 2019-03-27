from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from cs50 import get_int

a = get_int('a:')
b = get_int('b:')

x_knots = linspace(-3*pi, 3*pi, 201)
y_knots = linspace(-3*pi, 3*pi, 201)
X, Y = meshgrid(x_knots, y_knots)
R = sqrt(X**2+Y**2)
Z = cos(R)**2*exp(-0.1*R)
ax = Axes3D(figure(figsize=(8, 5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.hot, linewidth=0.4)
show()
