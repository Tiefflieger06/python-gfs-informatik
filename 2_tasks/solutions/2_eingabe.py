"""
Aufgabe 2: Benutzereingaben

Schreibe ein Programm, das:
1. Nach dem Namen des Benutzers fragt
2. Nach dem Alter des Benutzers fragt
3. Berechnet, in welchem Jahr der Benutzer geboren wurde
4. Eine Zusammenfassung ausgibt

Hinweis: Nutze input() für Eingaben und int() für Zahlenkonvertierung des Input-Strings.

Zusatzaufgabe: Frage nochmal nach dem Alter, falls die Eingabe nicht (nur) eine Zahl ist.

Erwartete Ausgabe (Beispiel):
Wie heißt du? [Max]
Wie alt bist du? [17]
Hallo Max, du wurdest vermutlich 2007 geboren!
"""

# Hier kommt dein Code hin

name = input("Wie heißt du? ")

while True:
    try:
        alter = int(input("Wie alt bist du? "))
        break
    except ValueError:
        print("Bitte gib eine gültige Zahl ein!")

geburtsjahr = 2025 - alter
print(f"Hallo {name}, du wurdest vermutlich {geburtsjahr} geboren!")
