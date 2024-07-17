import tkinter as tk

root = tk.Tk()

Label = tk.Label(root, text="Hallo Welt")
Label.pack()

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
