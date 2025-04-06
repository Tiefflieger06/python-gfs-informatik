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
