class Waschmaschnine:
    def __init__(self, name, marke, modell, kapazitaet, preis):
        self.name = name
        self.marke = marke
        self.modell = modell
        self.kapazitaet = kapazitaet
        self.preis = preis
        self.status = "frei"
        self.laenge = 0
        
    def waschen(self, marke, waschmittel, waschtemperatur, waschzeit):
        self.marke = marke
        self.status = "belegt"
        self.laenge = waschzeit
        print(f"Die Waschmaschine {self.marke}")
        print(f"Kake {self.marke}")
    
    def anzeigenInformationen(self):
        print(f"Die Waschmaschine {self.marke}")
        print(f"Kapazitaet {self.kapazitaet} kg")
        print(f"Preis {self.preis} Euro")
        print(f"Status {self.status}")
            
            

