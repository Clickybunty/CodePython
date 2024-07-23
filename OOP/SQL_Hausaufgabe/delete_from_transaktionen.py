import sqlite3

try:
    conn = sqlite3.connect('paypal_kundendaten.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM Transaktionen WHERE TransaktionsID = 1')
    conn.commit()
    print("Datensatz erfolgreich gelöscht.")
except sqlite3.Error as e:
    print(f"Fehler beim Löschen des Datensatzes: {e}")
finally:
    if conn:
        conn.close()
