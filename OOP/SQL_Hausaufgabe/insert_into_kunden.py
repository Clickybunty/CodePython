import sqlite3

try:
    conn = sqlite3.connect('paypal_kundendaten.db')
    cursor = conn.cursor()
    kunden_daten = [
        (1, 'John Doe', '123 Main St', 'john.doe@example.com'),
        (2, 'Jane Smith', '456 Oak Ave', 'jane.smith@example.com'),
        (3, 'Alice Johnson', '789 Pine Rd', 'alice.johnson@example.com'),
        (4, 'Bob Brown', '101 Maple St', 'bob.brown@example.com'),
        (5, 'Carol White', '202 Elm St', 'carol.white@example.com')
    ]
    cursor.executemany('INSERT INTO Kunden (KundenID, Name, Adresse, Email) VALUES (?, ?, ?, ?)', kunden_daten)
    conn.commit()
    print("Daten erfolgreich in die Tabelle 'Kunden' eingefügt.")
except sqlite3.Error as e:
    print(f"Fehler beim Einfügen der Daten: {e}")
finally:
    if conn:
        conn.close()
