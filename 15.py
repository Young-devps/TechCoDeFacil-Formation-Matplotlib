import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
# graph en live

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animated(i):
    graph_data = open('example.txt', 'r').read()
    lines = graph_data.split('\n')
    Xs = []
    Ys = []
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            Xs.append(x)
            Ys.append(y)
    ax1.clear()
    ax1.plot(Xs, Ys)

ani = animation.FuncAnimation(fig, animated, interval=1000)
plt.show()
