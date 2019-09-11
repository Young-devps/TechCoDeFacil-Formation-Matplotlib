import matplotlib.pyplot as plt
import random
from matplotlib import style
# subplot and subplot2grid
style.use('dark_background')
fig = plt.figure()

def create_plot():
    xs = []
    ys = []
    for i in range(10):
        x = i
        y = random.randrange(10)
        xs.append(x)
        ys.append(y)
    return xs, ys

# ax1 = plt.subplot2grid((6,1), (0,0), rowspan=1, colspan=1)
# ax2 = plt.subplot2grid((6,1), (1,0), rowspan=4, colspan=1)
# ax3 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1)


# # add subplot
# ax1 = plt.subplot(221)
# ax2 = plt.subplot(222)
# ax3 = plt.subplot(212)

x, y = create_plot()
ax1.plot(x,y)

x, y = create_plot()
ax2.plot(x, y)

x, y = create_plot()
ax3.plot(x, y)

plt.show()