# Importiert die Funktion
# create_database aus 
# dem Modul internet_DB
from internet_DB import create_database

# Importiert die Funktion
# insert_internet_data aus 
# dem Modul insert_data
from insert_data import insert_internet_data

# Importiert die Funktion
# fetch_internet_data aus 
# dem Modul fetch_data
from fetch_data import fetch_internet_data

# Importiert die Funktion 
# analyze_internet_data aus 
# dem Modul analyze_data
from analyze_data import analyze_internet_data

# Definiert die main() Funktion, 
# die die Hauptoperationen ausführt
def main():
    
    # Erstellt die Datenbank und die Tabelle
    create_database()
    
    # Fügt Daten in die Tabelle ein
    insert_internet_data()
    
    # Ruft die Daten aus der Tabelle ab
    data = fetch_internet_data()
        
    # Analysiert und visualisiert die abgerufenen Daten
    analyze_internet_data(data)

# Führt die main() Funktion aus, 
# wenn das Skript direkt ausgeführt wird
if __name__ == "__main__":
    main()