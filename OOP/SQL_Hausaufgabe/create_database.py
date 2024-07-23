import sqlite3

try:
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect('paypal_kundendaten.db')
    print("Datenbank 'paypal_kundendaten.db' erfolgreich erstellt.")
except sqlite3.Error as e:
    print(f"Fehler bei der Erstellung der Datenbank: {e}")
finally:
    if conn:
        conn.close()
