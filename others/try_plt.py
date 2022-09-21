import matplotlib.pyplot as plt

# x = [2002, 2006, 2010, 2014, 2018, 2022]
# y = [1.2, 1.9, 2.7, 3.1, 3.5, 3.8]

# # plt.plot(x, y, marker='o', linestyle='-', color='g', label='FIFA')
# # plt.bar(x, y, label='FIFA')
# # plt.pie(y, labels=x, autopct='%.0f %%')
# plt.xlabel('Years')
# plt.ylabel('Viewers (billion)')
# plt.title('FIFA Wold Cup viewers by edition')
# plt.legend(loc='upper left')
# # plt.xticks(x)
# plt.show()

#

# ages = [15, 16, 17, 30, 31, 32, 35]
# # bins = [15, 20, 25, 30, 35]

# # plt.hist(ages, bins, edgecolor='black')
# # plt.show()

# plt.boxplot(ages)
# plt.show()

#

# celui est comme placer des paires de coordonnees
# sur un plan cartesien (a: X, b: Y)
# len(a) == len(b)
a = [1, 2, 3, 4, 5, 4, 3, 5, 6, 7]
b = [7, 2, 3, 5, 5, 7, 2, 6, 3, 2]
colors = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
]

plt.scatter(a, b, c=colors, s=5)
plt.show()
