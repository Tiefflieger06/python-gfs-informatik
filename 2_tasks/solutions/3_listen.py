"""
Aufgabe 3: Listen und Schleifen

Erstelle ein Programm, das:
1. Eine Liste von Schulnoten enthält (1-6)
2. Die Durchschnittsnote berechnet
3. Die beste und schlechteste Note ausgibt
4. Alle Noten besser als 4 ausgibt

Erwartete Ausgabe (Beispiel):
Noten: [1, 3, 2, 4, 5, 2]
Durchschnitt: 2.83
Beste Note: 1
Schlechteste Note: 5
Gute Noten: 1, 3, 2, 2
"""

# Hier kommt dein Code hin

noten = [1, 3, 2, 4, 5, 2]

ges = 0
for note in noten:
    ges += note
durchschnitt = ges / len(noten)
beste = min(noten)
schlechteste = max(noten)

# Beispiel für "List Comprehension"
gute_noten = [note for note in noten if note <= 3]

print(f"Noten: {noten}")
print(f"Durchschnitt: {durchschnitt}")
print(f"Beste Note: {beste}")
print(f"Schlechteste Note: {schlechteste}")
print(f"Gute Noten: {', '.join(map(str, gute_noten))}")
