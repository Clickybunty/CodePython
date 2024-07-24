import sqlite3

def insert_weather_data():
    wetterdaten = [
('2023-07-01', 25.5, 60, 5.2),
('2023-07-02', 27.1, 55, 0.0),
('2023-07-03', 24.3, 70, 10.5),
('2023-07-04', 26.7, 65, 0.0),
('2023-07-05', 23.9, 80, 12.1),
]
    conn = sqlite3.connect('wetterdaten.db')
    cursor = conn.cursor()
    cursor.executemany('''
INSERT OR IGNORE INTO Wetter (Datum, Temperatur, Luftfeuchtigkeit,
Niederschlag)
VALUES (?, ?, ?, ?)
''', wetterdaten)
    conn.commit()
    conn.close()

def fetch_weather_data():
    conn = sqlite3.connect('wetterdaten.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Wetter')
    rows = cursor.fetchall()
    conn.close()
    data = {
'Datum': [row[0] for row in rows],
'Temperatur': [row[1] for row in rows],
'Luftfeuchtigkeit': [row[2] for row in rows],
'Niederschlag': [row[3] for row in rows]
}
    return data