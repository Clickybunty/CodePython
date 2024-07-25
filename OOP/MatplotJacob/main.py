import matplotlib.pyplot as plt 
 
# Balken    #   #   #   #   #   #   #   #   #   #   #   #   #   #   #       
produkte = ['Äpfel','Orangen','Bananen','Trauben']
anzahl = [30,15,25,10]

plt.bar(produkte, anzahl)
plt.xlabel('Produkte')
plt.ylabel('Anzahl')
plt.title('Meine Produkte')
plt.show()


# Torten
Firmen = ['Firma A', 'Firma B', 'Firma C', 'Firma D']
Proz = [40, 30, 20, 10]

plt.pie(Proz, labels=Firmen)
# plt.title('Torte')
plt.show()

Aktien = ['Tesla', 'Bitcoin', 'Meta',' Nvidia', 'Gold']
anteile = [10, 80, 3, 5, 2]