from OOP.Haushaltsgeraet import Waschmaschnine

# Die Klasse Auto wird referenziert
from OOP.AutoOOP import Auto

# Die Klasse Piepmatz wird refernziert
from OOP.VoegelOOP import Piepmatz

# Der Vogel Papagai wird als Objekt, 
# der Klasse Piepmatz Deklariert und Initialisiert
Papagai = Piepmatz("Pirat", "5", "21Kg", "Rot-Blau-Gelb")

# Methode wird aufgerufen die in der Klasse Piepmatz stecken
Papagai.fliegt()

# Der Vogel KanarienSpatz wird als Objekt, 
# der Klasse Piepmatz Deklariert und Initialisiert
KanarienSpatz = Piepmatz("Django", "4", "45Kg", "Aquamarin")

# Methode wird aufgerufen die in der Klasse Piepmatz stecken
KanarienSpatz.fliegt()

# Der Vogel meinPiepmatz wird als Objekt, 
# der Klasse Piepmatz Deklariert und Initialisiert
meinPiepmatz = Piepmatz("Hansi", "3", "5,7Kg", "Rot")

# Methode wird aufgerufen die in der Klasse Piepmatz stecken
meinPiepmatz.fliegt()

# Methode wird aufgerufen die in der Klasse Piepmatz stecken
meinPiepmatz.InformationenAnzeigen()

'''
# Waschmaschine
meineWaschmaschine = Waschmaschnine("Brummwasch", "Bosch", "X46012Kg", "7 Kg", "500")

meineWaschmaschine.waschen()
meineWaschmaschine.anzeigenInformationen()
'''

'''
# Das Objekt "Dudu" der Klasse "Auto" wird Deklariert und initalisiert.
Dudu = Auto("VW Käfer", "Busch", "2001", "Beige", "10.000.001")

# Methoden werden aufgerufen die in der Klasse Auto stecken
Dudu.starten()
Dudu.fahren()
Dudu.InformationenAnzeigen()
Dudu.Lackieren()
Dudu.Tanken()
'''

