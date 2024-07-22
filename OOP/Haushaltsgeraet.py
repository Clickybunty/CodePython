class Waschmaschnine:
    def __init__(self, name, marke, modell, kapazitaet, preis):
        self.name = name
        self.marke = marke
        self.modell = modell
        self.kapazitaet = kapazitaet
        self.preis = preis
        
    def waschen(self):     
        print(f"Die Waschmaschine {self.name}")
        print(f"Ist aus dem Hause {self.marke}")
    
    def anzeigenInformationen(self):
        print(f"Die Waschmaschine {self.marke}")
        print(f"Kapazitaet {self.kapazitaet} kg")
        print(f"Preis {self.preis} Euro")
            
            

