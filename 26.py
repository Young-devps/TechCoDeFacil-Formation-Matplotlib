# scatter plot

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


ax.scatter(X, Y, Z)
ax.scatter(Y, Z, X)

plt.show()