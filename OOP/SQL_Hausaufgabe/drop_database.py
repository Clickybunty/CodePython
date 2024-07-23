import os

try:
    if os.path.exists('paypal_kundendaten.db'):
        os.remove('paypal_kundendaten.db')
        print("Datenbank 'paypal_kundendaten.db' erfolgreich gelöscht.")
    else:
        print("Datenbank 'paypal_kundendaten.db' nicht gefunden.")
except Exception as e:
    print(f"Fehler beim Löschen der Datenbank: {e}")
