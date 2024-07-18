def finde_groesstes_element(liste): 
    groesstes = liste[0] 

    for zahl in liste:
        if zahl > groesstes: 
            groesstes = zahl 
    return groesstes 

def finde_kleinstes_element(liste): 
    kleinstes = liste[0] 

    for zahl in liste: 
        if zahl < kleinstes: 
            kleinstes = zahl 
    return kleinstes

def berechne_durchschnitt(liste): 
    summe = 0 

    for zahl in liste: 
        summe += zahl 
    durchschnitt = summe / len(liste) 
    return durchschnitt 

zahlen = [3, 5, 2, 8, 1, 4] 

groesste_zahl = finde_groesstes_element(zahlen) 

kleinste_zahl = finde_kleinstes_element(zahlen) 

durchschnitt_zahl = berechne_durchschnitt(zahlen) 

print("Die größte Zahl in der Liste ist: " + str(groesste_zahl))

print("Die kleinste Zahl in der Liste ist: " + str(kleinste_zahl)) 

print("Der Durchschnitt der Zahlen in der Liste ist: " + str(durchschnitt_zahl))

# Die größte Zahl in der Liste ist: 8
# Die kleinste Zahl in der Liste ist: 1
# Der Durchschnitt der Zahlen in der Liste ist: 3.8333333333333335