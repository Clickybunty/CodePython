import sqlite3

try:
    conn = sqlite3.connect('paypal_kundendaten.db')
    cursor = conn.cursor()
    transaktionen_daten = [
        (1, 1, 100.00, '2023-07-22'),
        (2, 2, 150.50, '2023-07-23'),
        (3, 3, 200.75, '2023-07-24'),
        (4, 4, 250.25, '2023-07-25'),
        (5, 5, 300.50, '2023-07-26')
    ]
    cursor.executemany('INSERT INTO Transaktionen (TransaktionsID, KundenID, Betrag, Datum) VALUES (?, ?, ?, ?)', transaktionen_daten)
    conn.commit()
    print("Daten erfolgreich in die Tabelle 'Transaktionen' eingefügt.")
except sqlite3.Error as e:
    print(f"Fehler beim Einfügen der Daten: {e}")
finally:
    if conn:
        conn.close()
