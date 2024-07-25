# Importiert die Funktion
# create_database aus 
# dem Modul db_setup
from db_setup import create_database

# Importiert die Funktion
# insert_sport_data und 
# fetch_sport_data aus 
# dem Modul insert_data
from insert_data import insert_sport_data, fetch_sport_data

# Importiert die Funktion
# analyze_sport_data aus 
# dem Modul matplot_data
from matplot_data import analyze_sport_data

# Definiert die main() Funktion, 
# die die Hauptoperationen ausführt
def main():
    
    # Dieser Funktionsaufruf erstellt die Datenbank !!!
    # conn = sqlite3.connect('sportergebnisse.db') und 
    #
    # die Tabelle     cursor.execute('''
    #    CREATE TABLE IF NOT EXISTS Ergebnisse (
    #        Datum TEXT,
    #        Team TEXT,
    #        Tore INTEGER,
    #        PRIMARY KEY (Datum, Team)
    #    )
    #''')
    create_database()
    
    # Dieser Funktionsaufruf erstellt eine Liste von Datensätzen
    # (Datum, Team, Tore), 
    # die in die Datenbank eingefügt werden sollen.
    insert_sport_data()
    
    
    # Erstellt eine Verbindung zur
    # `sportergebnisse.db` und 
    # ruft die Daten aus der Tabelle ab und legt sie
    # in die Variablen data als Dictionary ab
    data = fetch_sport_data()
    
    # Dieser Funktionsaufruf analysiert und visualisiert
    # die Funktion wandelt die Datumsangaben um, 
    # erstellen einer Liste aller Teamnamen im 'data'-Dictionary und
    # initialisiert eine neue Abbildung mit der Größe 10x6 
    analyze_sport_data(data)

# Prüft ob dieses Skript direkt ausgeführt wird
# Führt die main() Funktion aus, 
# wenn das Skript direkt ausgeführt wurde
if __name__ == "__main__":
    main()
