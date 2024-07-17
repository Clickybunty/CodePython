x = 1
while x == 1:
    print("**************************\nTaschenrechner x3100-f5000\n**************************")
    
    Zahl1=int(input("Geben Sie eine Zahl ein:  "))
    Operator=str(input("Wählen sie einen Operator  + ,  - ,  * ,  /  oder Modulo mit  % :  "))
    Zahl2=int(input("Geben Sie die zweite Zahl ein:  "))
    
    if Operator == "+":
        Ergebnis =  Zahl1 + Zahl2
    elif Operator == "-":
        Ergebnis =  Zahl1 - Zahl2
    elif Operator == "*":
        Ergebnis =  Zahl1 * Zahl2
    elif Operator == "/":
        Ergebnis =  Zahl1 / Zahl2
    elif Operator == "%":
        Ergebnis =  Zahl1 % Zahl2
    else:
        print("Fehler")
    
    
    print(Ergebnis)
    
    
    Abbruch=input("Mit 1 + Enter eine weitere Berechnug starten")
    if Abbruch == "0":
        x = 0
    elif Abbruch == "1":
        x = 1
    else:
        print("Hey falsche Eingabe man! x3100-f5000 AKTIV")
    