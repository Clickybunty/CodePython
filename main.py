from OOP.Haushaltsgeraet import Waschmaschnine
from OOP.AutoOOP import Auto
from OOP.VoegelOOP import Piepmatz

# Waschmaschine
meineWaschmaschine = Waschmaschnine("Brummwasch", "Bosch", "X46012Kg", "7 Kg", "500")
print(f"Die Waschmaschine {Waschmaschnine.marke} wird belegt")

meineWaschmaschine.waschen()
meineWaschmaschine.anzeigenInformationen()

# Auto
Dudu = Auto("VW Käfer", "Busch", "2001", "Beige", "10.000.001")

Dudu.starten()
Dudu.fahren()
Dudu.InformationenAnzeigen()

#Vogel
meinPiepmatz = Piepmatz("Hansi", "3", "5,7Kg", "Rot")

meinPiepmatz.fliegt()
meinPiepmatz.InformationenAnzeigen()