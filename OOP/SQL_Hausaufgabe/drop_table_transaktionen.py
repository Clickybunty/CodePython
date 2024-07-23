import sqlite3

try:
    conn = sqlite3.connect('paypal_kundendaten.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS Transaktionen')
    conn.commit()
    print("Tabelle 'Transaktionen' erfolgreich gelöscht.")
except sqlite3.Error as e:
    print(f"Fehler beim Löschen der Tabelle: {e}")
finally:
    if conn:
        conn.close()
