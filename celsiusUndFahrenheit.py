# ########## celsius_to_fahrenheit(celsius) ########## #
#                                            
#  *****************************************************
#  *****************************************************
#  **                                    
#  **    Autor: Stevan Menicanin         
#  **    Datum: 07-18-2024               
#  **    Version: 1.0                    
#  **    Beschreibung: Temperatur umrechnnung,
#  **                  Celsius nach Fahrenheit
#  **                                    
#  **    Parameters: €                   
#  **                Betrag in €         
#  **                zum Umrechnen in $  
#  **                                    
#  **    Connection:                     
#  **                                    
#  **    Link:                           
#  **                                    
#  *****************************************************  
#  *****************************************************  
#                                            
# ######################################################

# def leitet die generierung der Funktion ein
# celsius_to_fahrenheit(celsius) ist die Funktion und celsius ist der Parameter
# Diese Funktion wandelt eine Temperatur von Celsius in Fahrenheit um.
def celsius_to_fahrenheit(celsius):   
    # return gibt den wert der nachfolgenden variabel nach der berechnung zurück  
    return celsius * 9/5 + 32

# ########## fahrenheit_to_celsius(fahrenheit) ########## #
#                                            
#  *****************************************************
#  *****************************************************
#  **                                    
#  **    Autor: Stevan Menicanin         
#  **    Datum: 07-18-2024               
#  **    Version: 1.0                    
#  **    Beschreibung: Temperatur umrechnnung,
#  **                  Fahrenheit nach Celsius
#  **                                    
#  **    Parameters: €                   
#  **                Betrag in €         
#  **                zum Umrechnen in $  
#  **                                    
#  **    Connection:                     
#  **                                    
#  **    Link:                           
#  **                                    
#  *****************************************************  
#  *****************************************************  
#                                            
# ######################################################

# def leitet die generierung der Funktion ein
# fahrenheit_to_celsius(fahrenheit) ist die Funktion und Fahrenheit ist der Parameter
# Diese Funktion wandelt eine Temperatur von Fahrenheit in Celsius um.
def fahrenheit_to_celsius(fahrenheit):
    # return gibt den wert der nachfolgenden variabel nach der berechnung zurück  
    return (fahrenheit - 32) * 5/9

# Das Program fragt, welche Umrechnung durchgeführt werden soll
wahl = input("Möchten Sie Celsius in Fahrenheit (1) oder Fahrenheit in Celsius (2) umrechnen? ")

# try versucht den nachfolgenden code auszuführen.
# Wenn der code nicht ausgeführt werden kann, wird der nachfolgende code ausgeführt.
try:
    # Die Eingabe wird in eine Ganzzahl umgewandelt
    # int() wandelt den Typ der Eingabe in ein Integer um.
    wahl = int(wahl)
    # if prüft die nachfolgende bedingung 
    # if wahl == 1: ist True wenn wahl den Wert 1 hat
    if wahl == 1:
        # Wenn, Wahl 1 ist, dann wartet die Variable betrag_in_celsius auf die Eingabe
        betrag_in_celsius = float(input("Bitte geben Sie die Temperatur in Celsius ein: "))
        betrag_in_fahrenheit = celsius_to_fahrenheit(betrag_in_celsius)
        # Ausgabe der umgerechneten Temperatur in Fahrenheit
        # print ist eine Funktion die Text auf dem Bildschirm ausgiebt
        # f ermöglicht es Variabeln in den String, innerhalb der Geschweiften Klammern aufzurufen
        # die Variabeln werden mit dm Printbefehl mit ausgegeben.
        # .2f sorgt dafür, dass der Float 2 nachkommastellen hat.
        print(f"{betrag_in_celsius} Grad Celsius sind {betrag_in_fahrenheit:.2f} Grad Fahrenheit")
    # elif prüft die nachfolgende bedingung, wenn das forgestellte if False als ergebnis hat
    # elif wahl == 2: ist True wenn wahl den Wert 2 hat
    elif wahl == 2:
        # Wenn, Wahl 2 ist, dann wartet die Variable betrag_in_fahrenheit auf die Eingabe
        betrag_in_fahrenheit = float(input("Bitte geben Sie die Temperatur in Fahrenheit ein: "))
        betrag_in_celsius = fahrenheit_to_celsius(betrag_in_fahrenheit)
         # Ausgabe der umgerechneten Temperatur in Celsius
        # print ist eine Funktion die Text auf dem Bildschirm ausgiebt
        # f ermöglicht es Variabeln in den String, innerhalb der Geschweiften Klammern aufzurufen
        # die Variabeln werden mit dm Printbefehl mit ausgegeben.
        # .2f sorgt dafür, dass der Float 2 nachkommastellen hat.
        print(f"{betrag_in_fahrenheit} Grad Fahrenheit sind {betrag_in_celsius:.2f} Grad Celsius")
    # else prüft die nachfolgende bedingung, wenn das forgestellte elif False als ergebnis hat        
    else:
        # Wenn die Eingabe nicht 1 oder 2 ist, informiere den Benutzer über die ungültige Auswahl
        print("Ungültige Auswahl. Bitte wählen Sie 1 oder 2 für die Umrechnung.")
# Wenn der try versucht misslungen ist, wird except den Fehler abfangen 
# und den nachfolgenden Code ausführen
except ValueError:
    # print ist eine Funktion die Text auf dem Bildschirm ausgiebt
    # Fehlerbehandlung, falls die Eingabe keine gültige Zahl ist
    print("Fehler: Bitte geben Sie eine gültige Zahl für Ihre Auswahl ein.")