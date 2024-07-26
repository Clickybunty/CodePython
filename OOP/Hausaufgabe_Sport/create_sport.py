import sqlite3

def create_database():
    conn = sqlite3.connect('sportergebnisse.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Ergebnisse (
    Datum TEXT,
    Team TEXT,
    Tore INTEGER,
    PRIMARY KEY (Datum, Team)
    )
    ''')
    conn.commit()
    conn.close()