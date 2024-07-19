class Auto:
    def __init__(self, marke, modell, baujahr, farbe, kilometerstand):
        self.marke = marke
        self.modell = modell
        self.baujahr = baujahr
        self.farbe = farbe
        self.kilometerstand = kilometerstand
    
    def starten(self):
        print(f"Der Motor des {self.modell} wird gestartet")
                
    def fahren(self):
        print(f"Der {self.marke} setzt sich in bewegung")
        
    def InformationenAnzeigen(self):
        print(f"Marke: {self.marke}")
        print(f"Modell: {self.modell}")
        print(f"Baujahr: {self.baujahr}")
        print(f"Farbe: {self.farbe}")
        print(f"Kilometerstand: {self.kilometerstand}")
        
