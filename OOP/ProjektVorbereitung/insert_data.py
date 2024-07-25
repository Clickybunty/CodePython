# Importiert das sqlite3 Modul, 
# das für die Arbeit mit SQLite-Datenbanken in Python verwendet wird.
import sqlite3

# Erstellt eine Liste von Datensätzen
# (Datum, Team, Tore), 
# die in die Datenbank eingefügt werden sollen.
def insert_sport_data():
    
    # Beispielhafte Daten, 
    # die eingefügt werden sollen
    daten = [
        ('2023-08-01', 'Team A', 3),
        ('2023-08-01', 'Team B', 1),
        ('2023-08-02', 'Team A', 2),
        ('2023-08-02', 'Team C', 2),
        ('2023-08-03', 'Team B', 0),
        ('2023-08-03', 'Team C', 1),
    ]

    # Erstellt eine Verbindung zur
    # `sportergebnisse.db` und 
    # einen Cursor.
    conn = sqlite3.connect('sportergebnisse.db')
    cursor = conn.cursor()
    
    # Führt einen SQL-Befehl aus, 
    # der die Datensätze in die Tabelle
    # `sportergebnisse` einfügt. 
    # Mehrere Datensätze in die Tabelle "Ergebnisse" einfügen
    # Wenn der Primärschlüssel (Datum, Team) bereits existiert, 
    # wird der Datensatz ignoriert (INSERT OR IGNORE)
    cursor.executemany('''
        INSERT OR IGNORE INTO Ergebnisse (Datum, Team, Tore)
        VALUES (?, ?, ?)
    ''', daten)
    
    # Speichert die Änderungen in der Datenbank.
    conn.commit()
    
    # Schließt die Verbindung zur Datenbank.
    conn.close()

# Erstellt eine Verbindung zur
# `sportergebnisse.db` und 
# einen Cursor.
def fetch_sport_data():
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('sportergebnisse.db')
    cursor = conn.cursor()
    
    # Führt einen SQL-Befehl aus, 
    # der alle Daten aus der Tabelle
    # `Ergebnisse` abfragt. 
    # Die Ergebnisse werden in `rows` gespeichert.
    cursor.execute('SELECT * FROM Ergebnisse')
    rows = cursor.fetchall()
    
    # Verbindung zur Datenbank schließen
    conn.close()

    # Erstellt ein Dictionary
    # `data`, 
    # das die Daten in Listen für Datum, Team und 
    # Tore aufgeteilt.
    data = {
        'Datum': [row[0] for row in rows],
        'Team': [row[1] for row in rows],
        'Tore': [row[2] for row in rows]
    }
    
    # Gibt das Dictionary `data` zurück.
    return data
