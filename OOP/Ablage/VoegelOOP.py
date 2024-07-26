# Die Klasse Piepmatz wird deklariert
class Piepmatz:
    # Die Deklaration der Klasse Piepmatz
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
    
    # Die Methode der Klasse Piepmatz gibt hier den Namen des aufrufenden
    # Objekts der Klasse Piepmatz aus
    def fliegt(self):
        print(f"Der Vogel \"{self.name}\" fliegt")
        
    # Die Methode der Klasse Piepmatz gibt hier den Namenn das Alter, 
    # das Gewicht und die farbe des aufrufenden
    # Objekts der Klasse Piepmatz aus    
    def InformationenAnzeigen(self):
        print(f"Der Vogel hat den Namen \"{self.name}\"")
        print(f"Der Vogel ist {self.age} Jahre alt")
        print(f"Der Vogel wiegt {self.weight}")
        print(f"Der Vogel ist {self.color}")