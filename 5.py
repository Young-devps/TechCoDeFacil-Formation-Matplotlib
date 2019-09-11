import matplotlib.pyplot as plt

days = [1,2,3]

sleping = [5,7,3]
eating = [1,1,2]
sport = [3,4,2]
working = [10,14,12]

plt.plot([], [], color='b', label='sleping', linewidth=5)
plt.plot([], [], color='y', label='eating', linewidth=5)
plt.plot([], [], color='r', label='sport', linewidth=5)
plt.plot([], [], color='k', label='working', linewidth=5)

plt.stackplot(days, sleping, eating, sport, working, colors=['b', 'y', 'r', 'k'])

plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('learning \n matplotlib')

plt.legend()

plt.show()




















