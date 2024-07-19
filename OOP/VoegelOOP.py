class Piepmatz:
    def __init__(self, name, age, weight, color):
        self.name = name
        self.age = age
        self.weight = weight
        self.color = color
                
    def fliegt(self):
        print(f"Der Vogel \"{self.name}\" fliegt")
        
    def InformationenAnzeigen(self):
        print(f"Der Vogel hat den Namen \"{self.name}\"")
        print(f"Der Vogel ist {self.age} Jahre alt")
        print(f"Der Vogel wiegt {self.weight} Gramm")
        print(f"Der Vogel ist {self.color}")