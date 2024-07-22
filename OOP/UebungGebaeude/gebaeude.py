# Klasse
class Gebaeude:
    # Attribute
    def __init__(self, name, hoehe, bauweise, baujahr):
        self.name = name
        self.hoehe = hoehe 
        self.bauweise = bauweise
        self.baujahr = baujahr

    # Methoden
    def alter(self, aktuelles_jahr):
        return aktuelles_jahr - self.baujahr

    def ist_hoch(self):
        return self.hoehe > 100

    def sanierungsbedarf(self):
        if self.baujahr < 1950:
            return "Hoch"
        elif self.baujahr < 1980:
            return "Mittel"
        else:
            return "Niedrig"

    def umbauten(self, jahre):
        if jahre < 10:
            return "Keine Umbauten"
        elif jahre < 50:
            return "Einige Umbauten"
        else:
            return "Viele Umbauten"

    def __str__(self):
        return (f"Name: {self.name}, Höhe: {self.hoehe} m, "f"Bauweise: {self.bauweise}, Baujahr: {self.baujahr}")