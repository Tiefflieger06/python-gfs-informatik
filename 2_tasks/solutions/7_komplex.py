"""
Aufgabe 7: Textbasiertes Rollenspiel

Erstelle ein einfaches Rollenspiel-System mit folgenden Komponenten:

1. Klasse Charakter:
   - Attribute: name, lebenspunkte, stärke, inventar (Liste)
   - Methoden: 
     - angreifen(gegner)
     - heilen()
     - item_aufheben(item)

2. Klasse Spiel:
   - Attribute: spieler (Charakter), gegner (Liste von Charakteren), runde
   - Methoden:
     - kampf_starten()
     - status_anzeigen()
     - nächste_runde()

Beispiel Verwendung:
held = Charakter("Hero", 100, 15)
goblin = Charakter("Goblin", 50, 10)
spiel = Spiel(held, [goblin])
spiel.kampf_starten()

Zusatz: Nutze die random-Bibliothek für zufällige Schadenswerte beim Angriff.
"""

# Hier kommt dein Code hin

from random import randint

class Charakter:
    def __init__(self, name, lebenspunkte, stärke):
        self.name = name
        self.lebenspunkte = lebenspunkte
        self.stärke = stärke
        self.inventar = []

    def angreifen(self, gegner):
        schaden = randint(1, self.stärke)
        gegner.lebenspunkte -= schaden
        return f"{self.name} fügt {gegner.name} {schaden} Schaden zu!"

    def heilen(self):
        heilung = randint(5, 15)
        self.lebenspunkte += heilung
        return f"{self.name} heilt sich um {heilung} Lebenspunkte!"

    def item_aufheben(self, item):
        self.inventar.append(item)
        return f"{self.name} hat {item} aufgehoben!"

class Spiel:
    def __init__(self, spieler, gegner):
        self.spieler = spieler
        self.gegner = gegner
        self.runde = 0

    def status_anzeigen(self):
        print(f"\nRunde {self.runde}")
        print(f"{self.spieler.name}: {self.spieler.lebenspunkte} LP")
        for g in self.gegner:
            if g.lebenspunkte > 0:
                print(f"{g.name}: {g.lebenspunkte} LP")

    def kampf_starten(self):
        print("Kampf beginnt!")
        while self.spieler.lebenspunkte > 0 and any(g.lebenspunkte > 0 for g in self.gegner):
            self.nächste_runde()
        
        if self.spieler.lebenspunkte > 0:
            print(f"\n{self.spieler.name} hat gewonnen!")
        else:
            print("\nSpiel verloren!")

    def nächste_runde(self):
        self.runde += 1
        self.status_anzeigen()
        
        # Spielerzug
        for gegner in self.gegner:
            if gegner.lebenspunkte > 0:
                print(self.spieler.angreifen(gegner))
        
        # Gegnerzüge
        for gegner in self.gegner:
            if gegner.lebenspunkte > 0:
                print(gegner.angreifen(self.spieler))

# Beispielnutzung:
spieler = Charakter("Held", 100, 20)
gegner = [
    Charakter("Goblin", 30, 10),
    Charakter("Ork", 50, 15)
]
spiel = Spiel(spieler, gegner)
spiel.kampf_starten()
# Inventar-Beispiel:
spieler.item_aufheben("Schwert")
spieler.item_aufheben("Heiltrank")
print(f"Inventar: {spieler.inventar}")
