# matplotlib 3d basics
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
# or
X, Y, Z = axes3d.get_test_data(0.05)
print(type(X))
# Plot a basic wireframe.
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)

plt.show()