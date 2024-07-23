import sqlite3

try:
    conn = sqlite3.connect('paypal_kundendaten.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Transaktionen (
        TransaktionsID INT PRIMARY KEY,
        KundenID INT,
        Betrag DECIMAL(10, 2),
        Datum DATE,
        FOREIGN KEY (KundenID) REFERENCES Kunden(KundenID)
    )
    ''')
    print("Tabelle 'Transaktionen' erfolgreich erstellt.")
except sqlite3.Error as e:
    print(f"Fehler bei der Erstellung der Tabelle: {e}")
finally:
    if conn:
        conn.close()
