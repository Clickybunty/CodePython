from gebaeude import Gebaeude

# Klasse
class Wohngebaeude(Gebaeude):
    def __init__(self, name, hoehe, bauweise, baujahr, anzahl_wohnungen):
        super().__init__(name, hoehe, bauweise, baujahr)        
        self.anzahl_wohnungen = anzahl_wohnungen

    def __str__(self):
        return (super().__str__() + f", Anzahl Wohnungen: {self.anzahl_wohnungen}")