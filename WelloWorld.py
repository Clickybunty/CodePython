import random

def RandomFunc():
    RandNumber=(random.randint(1, 10))
    return RandNumber
i=0
while i<10:
    print(RandomFunc())
    i=i+1
    

# Function
name=input("Hey DU.. wie heißt Du? ")

def Modulo(Modu):
    return Modu % 2 == 0

def Begrueßung():    
    print(f"Hallo, {name}! Willkommen zum Python unterricht")

Begrueßung()

def ImQuadrat(Argument):
    return Argument * Argument

Input=int(input(name + " bitte gib eine Zahl ein um dessen Quadrat zu erhalten: "))

if Input >= 0:    
    Ergebnis=ImQuadrat(Input)
    print("Das Quadrat von "+ str(Input) + " ist: " + str(Ergebnis))
else:
    print("Die Zahl ist kleiner oder gleich Null")

InputPruefung = Modulo(Input)
if InputPruefung:
    print("Der Input Wert " + str(Input) +" ist gerade und")
else:
    print("Der Input Wert " + str(Input) +" ist ungrade und")
    
QuadratPruefung = Modulo(Ergebnis)
if  QuadratPruefung:
    print("Das Quadrat " + str(Ergebnis) +" ist gerade") 
else:
    print("Das Quadrat " + str(Ergebnis) +" ist ungrade")
    
