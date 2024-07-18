# ########## euro_to_dollar(euro) ########## #
#                                            #
#  ****************************************  #
#  ****************************************  #
#  **                                    **  #
#  **    Autor: Stevan Menicanin         **  #
#  **    Datum: 07-18-2024               **  #
#  **    Version: 1.0                    **  #
#  **    Beschreibung: Währungsrechner   **  #
#  **                                    **  #
#  **    Parameters: €                   **  #
#  **                Betrag in €         **  #
#  **                zum Umrechnen in $  **  #
#  **                                    **  #
#  **    Connection:                     **  #
#  **                                    **  #
#  **    Link:                           **  #
#  **                                    **  #
#  ****************************************  #
#  ****************************************  #
#                                            #
# ########################################## #

# Eine Funktion zur Umrechnung von Euro in Dollar
def euro_to_dollar(euro):
    return euro * 1.12  # Multipliziert den Euro-Betrag mit dem Wechselkurs 1.12, um Dollar zu erhalten

# ######### dollar_to_euro(dollar) ######### #
#                                            #
#  ****************************************  #
#  ****************************************  #
#  **                                    **  #
#  **    Autor: Stevan Menicanin         **  #
#  **    Datum: 07-18-2024               **  #
#  **    Version: 1.0                    **  #
#  **    Beschreibung: Währungsrechner   **  #
#  **                                    **  #
#  **    Parameters: €                   **  #
#  **                Betrag in $         **  #
#  **                zum Umrechnen in €  **  #
#  **                                    **  #
#  **    Connection:                     **  #
#  **                                    **  #
#  **    Link:                           **  #
#  **                                    **  #
#  ****************************************  #
#  ****************************************  #
#                                            #
# ########################################## #

# Eine Funktion zur Umrechnung von Dollar in Euro
def dollar_to_euro(dollar):
    return dollar / 1.12  # Dividiert den Dollar-Betrag durch den Wechselkurs 1.12, um Euro zu erhalten

# Abfrage, ob der Nutzer Euro in Dollar oder Dollar in Euro umrechnen möchte
wahl = input("Möchten Sie Euro zu Dollar (1) oder Dollar zu Euro (2) umrechnen? ")

# Überprüfen, ob der Nutzer die Umrechnung von Euro zu Dollar gewählt hat
if wahl == "1":
    # Abfrage des Betrags in Euro vom Nutzer
    betrag_in_euro = float(input("Bitte geben Sie den Betrag in Euro ein: "))
    # Umrechnung des eingegebenen Euro-Betrags in Dollar
    betrag_in_dollar = euro_to_dollar(betrag_in_euro)
    # Ausgabe des umgerechneten Dollar-Betrags
    print(f"{betrag_in_euro} Euro sind {betrag_in_dollar:.2f} Dollar")

# Überprüfen, ob der Nutzer die Umrechnung von Dollar zu Euro gewählt hat
elif wahl == "2":
    # Abfrage des Betrags in Dollar vom Nutzer
    betrag_in_dollar = float(input("Bitte geben Sie den Betrag in Dollar ein: "))
    # Umrechnung des eingegebenen Dollar-Betrags in Euro
    betrag_in_euro = dollar_to_euro(betrag_in_dollar)
    # Ausgabe des umgerechneten Euro-Betrags
    print(f"{betrag_in_dollar} Dollar sind {betrag_in_euro:.2f} Euro")

# Falls der Nutzer eine ungültige Auswahl trifft (weder "1" noch "2")
else:
    # Hinweis für den Nutzer, dass die Auswahl ungültig ist und sie "1" oder "2" wählen sollen
    print("Ungültige Auswahl. Bitte wählen Sie 1 oder 2 für die Umrechnung.")