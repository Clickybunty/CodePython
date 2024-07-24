import sqlite3

def create_database():
    conn = sqlite3.connect('wetterdaten.db')
    cursor = conn.cursor()
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Wetter (
Datum TEXT PRIMARY KEY,
Temperatur REAL,
Luftfeuchtigkeit REAL,
Niederschlag REAL
)
''')

    conn.commit()
    conn.close()