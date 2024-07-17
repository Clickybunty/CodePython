def listen_analyse(zahlen_liste):
    if not zahlen_liste:
        return {
            "Summe": 0,
            "Durchschnitt": 0,
            "Höchste Zahl": None,
            "Niedrigste Zahl": None
        }
    
    summe = sum(zahlen_liste)
    durchschnitt = summe / len(zahlen_liste)
    höchste_zahl = max(zahlen_liste)
    niedrigste_zahl = min(zahlen_liste)
    
    return {
        "Summe": summe,
        "Durchschnitt": durchschnitt,
        "Höchste Zahl": höchste_zahl,
        "Niedrigste Zahl": niedrigste_zahl
    }

# Beispielzahlen
zahlen = [3, 7, 1, 9, 4]

# Aufruf der Funktion und Ausgabe der Ergebnisse
ergebnis = listen_analyse(zahlen)
print(ergebnis)
