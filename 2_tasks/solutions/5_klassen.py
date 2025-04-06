"""
Aufgabe 5: Bibliotheksverwaltung

Erstelle ein kleines Bibliothekssystem mit folgenden Klassen:

1. Buch:
   - Attribute: titel, autor, isbn, ausgeliehen (bool) (Standardwert: False; kann durch "[...], ausgeliehen=True)" gesetzt werden)
   - Methoden: ausleihen(), zurückgeben()

2. Bibliothek:
   - Attribute: name, bücher (Liste von Buch-Objekten)
   - Methoden: 
     - buch_hinzufügen(buch)
     - buch_entfernen(isbn)
     - buch_suchen(titel)
     - zeige_alle_bücher()

Beispiel Verwendung:
buch = Buch("Python Programmierung", "Max Müller", "123-456-789")
bibliothek = Bibliothek("Stadtbibliothek")
bibliothek.buch_hinzufügen(buch)
"""

# Hier kommt dein Code hin

class Buch:
    def __init__(self, titel, autor, isbn, ausgeliehen=False):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn
        self.ausgeliehen = ausgeliehen

    def ausleihen(self):
        if not self.ausgeliehen:
            self.ausgeliehen = True
            return True
        return False

    def zurückgeben(self):
        self.ausgeliehen = False

class Bibliothek:
    def __init__(self, name):
        self.name = name
        self.bücher = []

    def buch_hinzufügen(self, buch):
        self.bücher.append(buch)

    def buch_entfernen(self, isbn):
        self.bücher = [b for b in self.bücher if b.isbn != isbn]

    def buch_suchen(self, titel):
        return [b for b in self.bücher if titel.lower() in b.titel.lower()]

    def zeige_alle_bücher(self):
        for buch in self.bücher:
            status = "ausgeliehen" if buch.ausgeliehen else "verfügbar"
            print(f"{buch.titel} von {buch.autor} ({buch.isbn}) - {status}")

# Beispielnutzung
if __name__ == "__main__":
    # Bibliothek erstellen
    stadtbibliothek = Bibliothek("Stadtbibliothek")

    # Bücher erstellen
    buch1 = Buch("Der Herr der Ringe", "J.R.R. Tolkien", "978-3-608-93981-1")
    buch2 = Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", "978-3-551-55741-3")
    buch3 = Buch("Die unendliche Geschichte", "Michael Ende", "978-3-522-17684-2")

    # Bücher zur Bibliothek hinzufügen
    stadtbibliothek.buch_hinzufügen(buch1)
    stadtbibliothek.buch_hinzufügen(buch2)
    stadtbibliothek.buch_hinzufügen(buch3)

    # Alle Bücher anzeigen
    print("Alle Bücher in der Bibliothek:")
    stadtbibliothek.zeige_alle_bücher()

    # Buch ausleihen
    if buch1.ausleihen():
        print(f"\n{buch1.titel} wurde erfolgreich ausgeliehen.")
    
    # Bücher mit "Harry" im Titel suchen
    print("\nSuche nach 'Harry':")
    gefundene_bücher = stadtbibliothek.buch_suchen("Harry")
    for buch in gefundene_bücher:
        print(f"Gefunden: {buch.titel}")

    # Aktualisierte Bücherliste anzeigen
    print("\nAktualisierte Bücherliste:")
    stadtbibliothek.zeige_alle_bücher()
