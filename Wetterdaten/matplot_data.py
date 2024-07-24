import matplotlib.pyplot as plt
from datetime import datetime

def analyze_weather_data(data):
# Konvertiere Datum in ein für matplotlib verständliches Format
    daten = [datetime.strptime(datum, '%Y-%m-%d') for datum in
    data['Datum']]
    plt.figure(figsize=(10, 6))
# Temperaturverlauf
    plt.subplot(3, 1, 1)
    plt.plot(daten, data['Temperatur'], marker='o')
    plt.title('Temperaturverlauf')
    plt.xlabel('Datum')
    plt.ylabel('Temperatur (°C)')
# Luftfeuchtigkeitsverlauf
    plt.subplot(3, 1, 2)
    plt.plot(daten, data['Luftfeuchtigkeit'], marker='o', color='orange')
    plt.title('Luftfeuchtigkeitsverlauf')
    plt.xlabel('Datum')
    plt.ylabel('Luftfeuchtigkeit (%)')

# Niederschlagsverlauf
    plt.subplot(3, 1, 3)
    plt.plot(daten, data['Niederschlag'], marker='o', color='green')
    plt.title('Niederschlagsverlauf')
    plt.xlabel('Datum')
    plt.ylabel('Niederschlag (mm)')
    plt.tight_layout()
    plt.show()