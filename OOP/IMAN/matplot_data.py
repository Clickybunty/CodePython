import matplotlib.pyplot as plt
from datetime import datetime

def analyze_sport_data(data):
    # Datumswerte in datetime-Objekte umwandeln
    daten = [datetime.strptime(datum, '%Y-%m-%d') for datum in data['Datum']]
    
    # Eine Liste einzigartiger Teamnamen erstellen
    teams = list(set(data['Team']))
    
    # Eine neue Figur für das Diagramm erstellen
    plt.figure(figsize=(10, 6))

    # Für jedes Team eine Linie im Diagramm zeichnen
    for team in teams:
        # Datumswerte für das aktuelle Team
        team_dates = [daten[i] for i in range(len(daten)) if data['Team'][i] == team]
        
        # Tore für das aktuelle Team
        team_scores = [data['Tore'][i] for i in range(len(daten)) if data['Team'][i] == team]
        
        # Linie im Diagramm zeichnen
        plt.plot(team_dates, team_scores, marker='o', label=team)

    # Titel des Diagramms festlegen
    plt.title('Leistung der Teams über die Saison hinweg')
    
    # Beschriftung der x-Achse
    plt.xlabel('Datum')
    
    # Beschriftung der y-Achse
    plt.ylabel('Tore pro Spiel')
    
    # Legende anzeigen
    plt.legend()
    
    # Layout des Diagramms anpassen
    plt.tight_layout()
    
    # Diagramm anzeigen
    plt.show()
