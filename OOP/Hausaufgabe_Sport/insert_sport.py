import sqlite3

def insert_sport_data():
    daten = [
    ('2023-08-01', 'Team A', 3),
    ('2023-08-01', 'Team B', 1),
    ('2023-08-02', 'Team A', 2),
    ('2023-08-02', 'Team C', 2),
    ('2023-08-03', 'Team B', 0),
    ('2023-08-03', 'Team C', 1),
    ]
    conn = sqlite3.connect('sportergebnisse.db')
    cursor = conn.cursor()
    cursor.executemany('''
    INSERT OR IGNORE INTO Ergebnisse (Datum, Team, Tore)
    VALUES (?, ?, ?)
    ''', daten)
    conn.commit()
    conn.close()