from db_setup import create_database
from insert_data import insert_sport_data, fetch_sport_data
from matplot_data import analyze_sport_data

def main():
    # Schritt 1: Datenbank erstellen
    create_database()
    
    # Schritt 2: Beispieldaten einfügen
    insert_sport_data()
    
    # Schritt 3: Daten abrufen
    data = fetch_sport_data()
    
    # Schritt 4: Daten analysieren und visualisieren
    analyze_sport_data(data)

# Prüfen, ob dieses Skript direkt ausgeführt wird
if __name__ == "__main__":
    main()
