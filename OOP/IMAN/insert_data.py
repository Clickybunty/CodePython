import sqlite3

def insert_sport_data():
    # Beispielhafte Daten, die eingefügt werden sollen
    daten = [
        ('2023-08-01', 'Team A', 3),
        ('2023-08-01', 'Team B', 1),
        ('2023-08-02', 'Team A', 2),
        ('2023-08-02', 'Team C', 2),
        ('2023-08-03', 'Team B', 0),
        ('2023-08-03', 'Team C', 1),
    ]

    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('sportergebnisse.db')
    
    # Ein Cursor-Objekt erstellen
    cursor = conn.cursor()
    
    # Mehrere Datensätze in die Tabelle "Ergebnisse" einfügen
    # Wenn der Primärschlüssel (Datum, Team) bereits existiert, wird der Datensatz ignoriert (INSERT OR IGNORE)
    cursor.executemany('''
        INSERT OR IGNORE INTO Ergebnisse (Datum, Team, Tore)
        VALUES (?, ?, ?)
    ''', daten)
    
    # Änderungen in der Datenbank speichern
    conn.commit()
    
    # Verbindung zur Datenbank schließen
    conn.close()

def fetch_sport_data():
    # Verbindung zur SQLite-Datenbank herstellen
    conn = sqlite3.connect('sportergebnisse.db')
    
    # Ein Cursor-Objekt erstellen
    cursor = conn.cursor()
    
    # Alle Datensätze aus der Tabelle "Ergebnisse" auswählen
    cursor.execute('SELECT * FROM Ergebnisse')
    
    # Alle ausgewählten Zeilen abrufen
    rows = cursor.fetchall()
    
    # Verbindung zur Datenbank schließen
    conn.close()

    # Die Daten in einem Dictionary speichern
    data = {
        'Datum': [row[0] for row in rows],
        'Team': [row[1] for row in rows],
        'Tore': [row[2] for row in rows]
    }
    
    # Das Dictionary zurückgeben
    return data
