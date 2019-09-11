import matplotlib.pyplot as plt

# bars agains histograms



population_ages = [54,54, 87,6,2, 130, 78,49,96,32,32,44,54,32,115,87,132,32,32,23,36,98,87,74,41,12,25,58,56,64,69,67,82,23,21,24,2,100,101,123]

ids = [x for x in range(len(population_ages))]

bins = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

#plt.bar(ids, population_ages)
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('xlabel')
plt.ylabel('ylabel')

plt.title('learning \n matplotlib')

plt.legend()

plt.show()