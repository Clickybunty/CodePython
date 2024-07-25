# Die Klasse Auto wird deklariert
class Auto:
    # Deklaration 
    def __init__(self, marke, modell, baujahr, farbe, kilometerstand):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.farbe = farbe
        self.kilometerstand = kilometerstand
    
    # Methode starten: Gibt die Informaton aus, 
    # dass das Modell des Objekts der Klasse Auto gestartet wird
    def starten(self):
        print(f"Der Motor des {self.modell} wird gestartet")
    
    # Methode fahren: Gibt die Information aus,
    # dass die Marke des Objekts der Klasse Auto gefahren wird
    def fahren(self):
        print(f"Der {self.marke} setzt sich in bewegung")
    
    # Methode InformationenAnzeigen: Zeigt die Informationen 
    # des Modells (Objekts) der Klasse Auto an
    def InformationenAnzeigen(self):
        print(f"Marke: {self.marke}")
        print(f"Modell: {self.modell}")
        print(f"Baujahr: {self.baujahr}")
        print(f"Farbe: {self.farbe}")
        print(f"Kilometerstand: {self.kilometerstand}")
    
    # Die Methode Tanken zeigt die Information, 
    # dass die Marke des Objekts der Klasse Auto
    # getankt wird
    def Tanken(self):
        print(f"Der Tank vom {self.marke} ist in Reserve, \n Fahren Sie die nächste Tankstelle an!")    
        print(f"Der Tank des {self.modell} wird gefüllt")
        print(f"Der {self.marke} ist begetankt!")
    
    # Die Methode Lackieren zeigt die Farbe des Objektes der Klasse Auto an und
    # fragt nach einer Farbe in die das Auto umlackiert werden soll.
    # anschließend wird die Neue Farbe ausgegeben und eine gute weiterfahrt gewünscht.
    def Lackieren(self):
        print(f"Das Auto ist {self.farbe}")
        self.farbe = input(f"In welche Farbe soll der {self.marke} umlackiert werden? ")
        print(f"Der {self.marke} ist in {self.farbe} umlackiert, gute Fahrt")