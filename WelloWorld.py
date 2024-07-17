import tkinter as tk

root = tk.Tk()

# Benennt die Kopfzeile des GUI
root.title("Haed vom Fenster")

# Definiert die Größe der GUI
root.geometry("400x400")

# Beschränkt die Kleinste GUI Darstellung
root.minsize(width=200, height=200)

# Beschränkt die maximale GUI Darstellung
root.maxsize(width=800, height=800)

# Ein Label innerhalb des GUI
Label = tk.Label(root, text="Hallo Welt")
Label.pack()

# mainloop startet eine endlos schleife. 
# Code darunter kann erst mal nicht ausgeführt werden
# bis der mainloop beendet wird
root.mainloop()




def quiz():    
    Frage = input(Name + " Wie lautet die UID des Benutzers root? 1, -1, 255, 0, 65536 ")
    
    try:
        Frage = int(Frage)    
    except ValueError:
        print(Name + " versuche es noch einmal!")
        
    if Frage == 0:
        print("Richtig")
    elif Frage!=0:
        print("Falsch")
        print("Falsch")
        print("Super Falsch")
        
Name=input("Wie lautet dein Name? ")
print("Du behauptest also, dass dein Name " + Name + " lautet")
QuizStarten=input("Möchtest Du " + Name + " eine Quizfrage beantworten, dann schreibe Ja: ")

if QuizStarten.lower()!="ja":
    print("Schade dass Du nicht am Quiz teil nimmst. Auf wiedersehen " + Name)
elif QuizStarten.lower()=="ja":
    quiz()
else:
    print("Du hast nicht Ja geschrieben. Auf wiedersehen " + Name)
