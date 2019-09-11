# 3d bar charts
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Grab some test data.
liste = [4,5,6,8,7,3,1,2,4,9]
X = np.arange(10).reshape(2,5)
Y = np.full((2,5), 3)
Z = np.array(liste).reshape(2,5)

ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
ax.scatter(X, Y, Z) # can apply marker and color
ax.scatter(Y, Z, X)

dx = np.ones(10)
dy = np.ones(10)
dz = np.array([1,2,3,4,5,6,7,8,9,10])

ax.bar3d(X, Y, Z, dx, dy, dz)

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z label')

plt.show()