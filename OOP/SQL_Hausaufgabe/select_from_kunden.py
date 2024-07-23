import sqlite3

try:
    conn = sqlite3.connect('paypal_kundendaten.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Kunden WHERE KundenID = 1')
    result = cursor.fetchone()
    print(result)
except sqlite3.Error as e:
    print(f"Fehler bei der Abfrage: {e}")
finally:
    if conn:
        conn.close()
