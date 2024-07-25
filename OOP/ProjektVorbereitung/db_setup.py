# Importiert das sqlite3 Modul, 
# das für die Arbeit mit SQLite-Datenbanken in Python verwendet wird.
import sqlite3

# Methode zum erstellen einer DB
def create_database():
    
    # Erstellt eine Verbindung zu einer SQLite-Datenbank 
    # namens `sportergebnisse.db`. 
    # Wenn die Datei nicht existiert, 
    # wird sie erstellt.
    conn = sqlite3.connect('sportergebnisse.db')
    
    # Erstellt ein Cursor-Objekt, 
    # das für die Ausführung von 
    # SQL-Befehlen verwendet wird.
    cursor = conn.cursor()
    
    # Führt einen SQL-Befehl aus, 
    # der eine Tabelle namens `Internetverbrauch` erstellt, 
    # wenn sie nicht bereits existiert. 
    # Die Tabelle hat zwei Spalten:
    # `Datum` (Text, Primärschlüssel) und 
    # `Verbrauch` (Reellwert).
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ergebnisse (
            Datum TEXT,
            Team TEXT,
            Tore INTEGER,
            PRIMARY KEY (Datum, Team)
        )
    ''')
    
    # Speichert die Änderungen in der Datenbank.
    conn.commit()
    
    # Schließt die Verbindung zur Datenbank.
    conn.close()
