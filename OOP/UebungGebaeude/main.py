# Import der Klassen
from gebaeude import Gebaeude
from wohngebaeude import Wohngebaeude

# Objekte
hochhaus = Gebaeude("Empire State Building", 381, "Stahlbauweise", 1931)

einfamilienhaus = Gebaeude("Schmidt's Haus", 7, "Massivbauweise", 2015)

kirche = Gebaeude("Kölner Dom", 157, "Gotische Bauweise", 1880)

# Neues Objekt der abgeleiteten Klasse
wohngebaeude = Wohngebaeude("Wohnkomplex", 50, "Betonbauweise", 1990, 120)

# Methodenaufruf
print(f"{hochhaus.name}: Alter: {hochhaus.alter(2024)} Jahre, Hoch:{hochhaus.ist_hoch()}, Sanierungsbedarf: {hochhaus.sanierungsbedarf()},Umbauten: {hochhaus.umbauten(93)}")
print(f"{einfamilienhaus.name}: Alter: {einfamilienhaus.alter(2024)} Jahre,Hoch: {einfamilienhaus.ist_hoch()}, Sanierungsbedarf:{einfamilienhaus.sanierungsbedarf()}, Umbauten:{einfamilienhaus.umbauten(9)}")
print(f"{kirche.name}: Alter: {kirche.alter(2024)} Jahre, Hoch:{kirche.ist_hoch()}, Sanierungsbedarf: {kirche.sanierungsbedarf()},Umbauten: {kirche.umbauten(144)}")
print(f"{wohngebaeude.name}: {wohngebaeude}")