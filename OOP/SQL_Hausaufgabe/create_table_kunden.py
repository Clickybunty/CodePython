import sqlite3

try:
    conn = sqlite3.connect('paypal_kundendaten.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Kunden (
        KundenID INT PRIMARY KEY,
        Name VARCHAR(100),
        Adresse VARCHAR(255),
        Email VARCHAR(100)
    )
    ''')
    print("Tabelle 'Kunden' erfolgreich erstellt.")
except sqlite3.Error as e:
    print(f"Fehler bei der Erstellung der Tabelle: {e}")
finally:
    if conn:
        conn.close()
