# 3d bar charts
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x, y, z = axes3d.get_test_data()
print(axes3d.__file__)
ax.plot_wireframe(x,y,z, rstride=5, cstride=5)

ax.set_xlabel('x axis')
ax.set_ylabel('y axis')
ax.set_zlabel('z label')

plt.show()