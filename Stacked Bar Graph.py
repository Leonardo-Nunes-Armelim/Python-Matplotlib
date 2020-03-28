import matplotlib.pyplot as plt

car_1 = (15, 40, 24, 28, 12)
car_2 = (40, 28, 40, 26, 35)

index = [0, 1, 2, 3, 4]
width = 0.4

plt.title('Sales by car type')

plt.xticks(index, ('Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'))
bar_1 = plt.bar(index, car_1, width)
bar_2 = plt.bar(index, car_2, width, bottom=car_1)

plt.ylabel('Sales')
plt.yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

plt.legend((bar_1[0], bar_2[0]), ('Car_1', 'Car_2'))

plt.show()