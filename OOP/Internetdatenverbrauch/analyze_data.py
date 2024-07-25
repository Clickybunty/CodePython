# Importiert das matplotlib.pyplot Modul, 
# das für die Erstellung von Diagrammen und 
# Visualisierungen in Python verwendet wird.
import matplotlib.pyplot as plt

# Importiert die datetime Klasse aus dem datetime Modul, 
# um Datum- und Uhrzeitoperationen durchzuführen.
from datetime import datetime

# Konvertiert die Datumsangaben von Strings zu `datetime` Objekten.
def analyze_internet_data(data):
    daten = [datetime.strptime(datum, '%Y-%m-%d') for datum in
    data['Datum']]

    # Erstellt eine neue Figure für das 
    # Diagramm mit der angegebenen Größe (10x6 Zoll).
    plt.figure(figsize=(10, 6))

    # Plottet die Verbrauchsdaten gegen die 
    # Datumsangaben mit Markern an den Datenpunkten.
    plt.plot(daten, data['Verbrauch'], marker='o')
    
    # Setzt den Titel und die Achsenbeschriftungen für das Diagramm.
    plt.title('Internetverbrauch')
    plt.xlabel('Datum')
    plt.ylabel('Verbrauch (GB)')

    # Passt das Layout des Diagramms an und zeigt es an.
    plt.tight_layout()
    plt.show()