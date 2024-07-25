import matplotlib.pyplot as plt

# Diese Zeile importiert das numpy-Modul und 
# gibt ihm den Alias np. 
# numpy ist ein Paket für wissenschaftliches Rechnen in Python und 
# bietet Unterstützung für große, 
# mehrdimensionale Arrays und 
# Matrizen sowie eine große Sammlung mathematischer Funktionen.
import numpy as np

# Diese Zeile wendet einen Stil namens _mpl-gallery auf 
# die matplotlib-Plots an. 
# Stile in matplotlib ändern das Aussehen der Plots, 
# wie Farben, 
# Linienbreiten und Hintergrundfarben.
plt.style.use('_mpl-gallery')

# Die Funktion np.random.seed(1) setzt 
# den Seed des Zufallsgenerators. 
# Dies sorgt dafür, 
# dass die zufälligen Zahlen, 
# die danach erzeugt werden, 
# jedes Mal gleich sind, 
# wenn der Code ausgeführt wird. 
# Dies ist nützlich für die 
# Reproduzierbarkeit von Ergebnissen.
np.random.seed(1)

# Diese Zeile erzeugt ein Array x mit 100 zufälligen Zahlen, 
# die aus einer Normalverteilung mit Mittelwert 0 und 
# Standardabweichung 1.5 stammen. 
# Diese Zahlen werden dann um 4 verschoben, 
# sodass der neue Mittelwert 4 ist.
x = 4 + np.random.normal(0, 1.5, 100)

# Diese Zeile erstellt ein neues 
# Figure-Objekt fig und 
# ein Axes-Objekt ax mit plt.subplots(). 
# fig ist das gesamte Bild oder 
# die Figur und 
# ax ist ein Teilbereich des Bildes, 
# in dem die Daten geplottet werden.
fig, ax = plt.subplots()

# Diese Zeile erstellt ein Histogramm 
# der Daten x auf dem Axes-Objekt ax. 
# Die Daten werden in 8 Bins aufgeteilt. 
# Die Parameter linewidth=0.5 und 
# edgecolor="white" geben an, 
# dass die Kanten der Bins eine Breite von 0.5 haben und 
# weiß eingefärbt sind.
ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")

# Diese Zeilen setzen die Grenzen und 
# Ticks der x- und y-Achsen. 
# xlim=(0, 8) setzt die Grenzen der x-Achse 
# von 0 bis 8. xticks=np.arange(1, 8) setzt 
# die x-Achsen-Ticks von 1 bis 7. 
# ylim=(0, 56) setzt die Grenzen der y-Achse von 0 bis 56. 
# yticks=np.linspace(0, 56, 9) setzt 9 gleichmäßig verteilte 
# y-Achsen-Ticks von 0 bis 56.
ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 56), yticks=np.linspace(0, 56, 9))

# Diese Zeile zeigt das erstellte Plot an. 
# plt.show() ist notwendig, 
# um das Diagramm in einem interaktiven Fenster anzuzeigen, 
# wenn der Code in einer Skriptdatei oder 
# einer nicht-interaktiven Umgebung ausgeführt wird.
plt.show()