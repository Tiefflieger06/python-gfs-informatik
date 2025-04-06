"""
Aufgabe 6: Zufallsgenerator

Erstelle ein Programm mit folgenden Funktionen:

1. würfeln(anzahl, seiten): Simuliert das Würfeln mit beliebig vielen Würfeln beliebiger Seitenzahl
2. zufallsgedicht(): Erstellt ein zufälliges Gedicht aus vorgegebenen Wörtern
3. glückskeks(): Gibt einen zufälligen Glückskeks-Spruch aus einer Liste aus
4. münzwurf(anzahl): Simuliert eine bestimmte Anzahl Münzwürfe und gibt die Statistik aus

Beispiele:
würfeln(3, 6) -> "Würfel: [3, 6, 1], Summe: 10"
zufallsgedicht() -> "Der kleine Hund, am grünen Grund, macht heute eine Rund"
glückskeks() -> "Deine Zukunft liegt in deinen Händen!"
münzwurf(100) -> "Kopf: 48%, Zahl: 52%"

Tipp: Nutze from random import choice, randint für Zufallszahlen. Nutze help(choice ODER randint) für mehr Informationen.
"""

# Hier kommt dein Code hin

from random import choice, randint

def würfeln(anzahl, seiten):
    ergebnisse = [randint(1, seiten) for _ in range(anzahl)]
    return f"Würfel: {ergebnisse}, Summe: {sum(ergebnisse)}"

def zufallsgedicht():
    subjekte = ["Hund", "Katze", "Maus", "Vogel"]
    orte = ["Haus", "Garten", "Wald", "See"]
    verben = ["läuft", "springt", "tanzt", "singt"]
    return f"Der {choice(subjekte)} im {choice(orte)} {choice(verben)} herum"

def glückskeks():
    sprüche = [
        "Deine Zukunft liegt in deinen Händen!",
        "Eine Überraschung wartet auf dich!",
        "Heute ist dein Glückstag!",
        "Eine Reise steht bevor!"
    ]
    return choice(sprüche)

def münzwurf(anzahl):
    würfe = [choice(["Kopf", "Zahl"]) for _ in range(anzahl)]
    kopf = würfe.count("Kopf")
    return f"Kopf: {kopf/anzahl*100:.0f}%, Zahl: {(anzahl-kopf)/anzahl*100:.0f}%"

# Beispielnutzung:
print(würfeln(3, 6))          # Würfelt 3x mit einem 6-seitigen Würfel
print(zufallsgedicht())       # Generiert ein zufälliges Gedicht
print(glückskeks())           # Gibt einen zufälligen Glückskeksspruch aus
print(münzwurf(50))         # Wirft 1000x eine Münze und zeigt die Verteilung
