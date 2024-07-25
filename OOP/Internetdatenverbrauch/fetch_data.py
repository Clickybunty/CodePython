# Importiert das sqlite3 Modul, 
# das für die Arbeit mit SQLite-Datenbanken in Python verwendet wird.
import sqlite3                  
    
# Importiert die datetime Klasse aus dem datetime Modul, 
# um Datum- und Uhrzeitoperationen durchzuführen.    
from datetime import datetime

# Erstellt eine Verbindung zur
# `internetdaten.db` und 
# einen Cursor.
def fetch_internet_data():
    conn = sqlite3.connect('internetdaten.db')
    cursor = conn.cursor()
    
    # Führt einen SQL-Befehl aus, 
    # der alle Daten aus der Tabelle
    # `Internetverbrauch` abfragt. 
    # Die Ergebnisse werden in `rows` gespeichert.
    cursor.execute('SELECT * FROM Internetverbrauch')
    rows = cursor.fetchall()
    
    # Schließt die Verbindung zur Datenbank.
    conn.close()
    # Erstellt ein Dictionary
    # `data`, 
    # das die Daten in Listen für Datum und 
    # Verbrauch aufgeteilt.
    data = {
'Datum': [row[0] for row in rows],
'Verbrauch': [row[1] for row in rows]
}
    # Gibt das Dictionary `data` zurück.
    return data