import sqlite3
import matplotlib.pyplot as plt
from datetime import datetime

#
def create_database():
    conn = sqlite3.connect('internetdaten.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Internetverbrauch (
            Datum TEXT PRIMARY KEY,
            Verbrauch REAL
        )
    ''')
    conn.commit()
    conn.close()
#
def insert_internet_data():
    daten = [
        ('2023-07-01', 2.5),
        ('2023-07-02', 3.1),
        ('2023-07-03', 2.0),
        ('2023-07-04', 4.3),
        ('2023-07-05', 3.7),
    ]
    #
    conn = sqlite3.connect('internetdaten.db')
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT OR IGNORE INTO Internetverbrauch (Datum, Verbrauch)
        VALUES (?, ?)
    ''', daten)
    conn.commit()
    conn.close()
#
def fetch_internet_data():
    conn = sqlite3.connect('internetdaten.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Internetverbrauch')
    rows = cursor.fetchall()
    conn.close()
    # 
    data = {
        'Datum': [row[0] for row in rows],
        'Verbrauch': [row[1] for row in rows]
    }
    #
    return data
#
def analyze_internet_data(data):
    daten = [datetime.strptime(datum, '%Y-%m-%d') for datum in data['Datum']]
    #
    plt.figure(figsize=(10, 6))
    #
    plt.plot(daten, data['Verbrauch'], marker='o')
    plt.title('Internetverbrauch')
    plt.xlabel('Datum')
    plt.ylabel('Verbrauch (GB)')
    #
    plt.tight_layout()
    plt.show()
#
def main():
    create_database()
    insert_internet_data()
    data = fetch_internet_data()
    analyze_internet_data(data)
#
if __name__ == "__main__":
    main()