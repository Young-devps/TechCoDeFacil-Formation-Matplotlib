import matplotlib.pyplot as plt

days = [1,2,3]

sleping = [5,7,3]
eating = [1,1,2]
sport = [3,4,2]
working = [10,14,12]

slices = [7,2,13,3]
activities = ['sleping', 'eating', 'sport', 'working']
cols = ['b','y','r','k']

plt.pie(slices, labels=activities, colors=cols, explode=(0,0.1,0,0), startangle=90, shadow=True, autopct='%1.1f%%')

# plt.xlabel('xlabel')
# plt.ylabel('ylabel')

plt.title('learning \n matplotlib')
plt.legend()
plt.show()




