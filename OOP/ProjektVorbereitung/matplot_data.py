# Importiert die Funktion
# analyze_sport_data aus 
# dem Modul matplot_data
import matplotlib.pyplot as plt
from datetime import datetime

# Diese Funktion Wandelt die Datumsangaben um, 
# erstellen einer Liste aller Teamnamen im 'data'-Dictionary und
# initialisiert eine neue Abbildung mit der Größe 10x6 
def analyze_sport_data(data):
    
    # Wandelt die Datumsangaben um
    # von Datumswerte in datetime-Objekte
    daten = [datetime.strptime(datum, '%Y-%m-%d') for datum in data['Datum']]
    
    # Erstellen einer Liste aller Teamnamen im 'data'-Dictionary
    # Sets stellt sicher, 
    # dass jedes Team nur einmal in der Liste vorkommt
    teams = list(set(data['Team']))
    
    # Initialisiert eine neue Abbildung mit der Größe 10x6 
    # für das Plotten der Daten
    plt.figure(figsize=(10, 6))

    # Schleife über jedes Team in der 'teams'-Liste, um deren Daten zu plotten
    # Für jedes Team eine Linie im Diagramm zeichnen
    for team in teams:
        
        # Erstellt eine Liste von Datumswerten für das aktuelle Team
        # Filtern der 'daten'-Liste nach dem Teamnamen aus 'data'
        team_dates = [daten[i] for i in range(len(daten)) if data['Team'][i] == team]
        
        # Erstellt eine Liste von Torewerten für das aktuelle Team
        # Filtert 'data['Tore']'-Liste nach Teamnamen aus 'data'
        team_scores = [data['Tore'][i] for i in range(len(daten)) if data['Team'][i] == team]
        
        # Zeichnet die Daten des aktuellen Teams in das Diagramm
        # 'team_dates' enthält die x-Werte (Datumsangaben), 
        # 'team_scores' enthält die y-Werte (Tore)
        # 'marker='o'' setzt Marker auf die Datenpunkte, 
        # 'label=team' fügt eine Beschriftung hinzu
        plt.plot(team_dates, team_scores, marker='o', label=team)

    # Setzt den Titel des Diagramms
    plt.title('Leistung der Teams über die Saison hinweg')
    
    # Beschriftet die x-Achse
    plt.xlabel('Datum')
    
    # Beschriftet die y-Achse
    plt.ylabel('Tore pro Spiel')
    
    # Fügt eine Legende hinzu, um die Linien dann den Teams zuzuordnen
    plt.legend()
    
    # Das Layout wird angepasst, 
    # um sicherzustellen, 
    # dass alles korrekt angezeigt wird
    plt.tight_layout()
    
    # Zeigt das Diagramm an
    plt.show()
