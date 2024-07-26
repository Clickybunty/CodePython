import sqlite3

def fetch_sport_data():
    conn = sqlite3.connect('sportergebnisse.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Ergebnisse')
    rows = cursor.fetchall()
    conn.close()
    data = {
    'Datum': [row[0] for row in rows],
    'Team': [row[1] for row in rows],
    'Tore': [row[2] for row in rows]
    }
    return data