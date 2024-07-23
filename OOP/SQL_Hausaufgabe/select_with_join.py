import sqlite3

try:
    conn = sqlite3.connect('paypal_kundendaten.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT Kunden.Name, Transaktionen.Betrag, Transaktionen.Datum
    FROM Kunden
    JOIN Transaktionen ON Kunden.KundenID = Transaktionen.KundenID
    ''')
    results = cursor.fetchall()
    for row in results:
        print(row)
except sqlite3.Error as e:
    print(f"Fehler bei der Abfrage: {e}")
finally:
    if conn:
        conn.close()
