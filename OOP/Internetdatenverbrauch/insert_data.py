# Importiert das sqlite3 Modul, 
# das für die Arbeit mit SQLite-Datenbanken in Python verwendet wird.
import sqlite3

# Erstellt eine Liste von Datensätzen
# (Datum, Verbrauch), 
# die in die Datenbank eingefügt werden sollen.
def insert_internet_data():
    daten = [
('2023-07-01', 2.5),
('2023-07-02', 3.1),
('2023-07-03', 2.0),
('2023-07-04', 4.3),
('2023-07-05', 3.7),
]
    # Erstellt eine Verbindung zur
    # `internetdaten.db` und 
    # einen Cursor.
    conn = sqlite3.connect('internetdaten.db')
    cursor = conn.cursor()
    
    # Führt einen SQL-Befehl aus, 
    # der die Datensätze in die Tabelle
    # `Internetverbrauch` einfügt. 
    # Wenn ein Datensatz mit demselben Primärschlüssel
    # (Datum) bereits existiert, 
    # wird er ignoriert.
    cursor.executemany('''
INSERT OR IGNORE INTO Internetverbrauch (Datum, Verbrauch)
VALUES (?, ?)
''', daten)
    
    # Speichert die Änderungen in der Datenbank.
    conn.commit()
    
    # Schließt die Verbindung zur Datenbank.
    conn.close()