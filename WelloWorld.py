import matplotlib.pyplot

x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

matplotlib.pyplot.plot(x, y)
matplotlib.pyplot.xlabel('x-Achse')
matplotlib.pyplot.ylabel('Y-Achse')
matplotlib.pyplot.title('Einfaches Liniendiagram')
matplotlib.pyplot.show()