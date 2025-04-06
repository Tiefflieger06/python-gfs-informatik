"""
Aufgabe 4: Funktionen und Bedingungen

Erstelle folgende Funktionen:
1. ist_palindrom(text): Prüft, ob ein Text vorwärts und rückwärts gleich ist
2. zensiere(text): Ersetzt alle Vokale (a,e,i,o,u) durch '*'. Tipp: Nutze TEXTVARIABLE.replace()
3. zaehle_worte(text): Zählt die Anzahl der Wörter in einem Text. Führe die Zeile help("".split) für einen Hinweis aus.

Beispiel:
ist_palindrom("otto") -> True
ist_palindrom("python") -> False
zensiere("Hallo Welt") -> "H*ll* W*lt"
zaehle_worte("Python ist cool") -> 3
"""

# Hier kommt dein Code hin

def ist_palindrom(text):
    text = text.lower()
    return text == text[::-1]

def zensiere(text):
    for vokal in 'aeiouAEIOU':
        text = text.replace(vokal, '*')
    return text

def zaehle_worte(text):
    return len(text.split())

# Beispiele
print(ist_palindrom("otto"))  # True
print(ist_palindrom("python"))  # False
print(zensiere("Hallo Welt"))  # H*ll* W*lt
print(zaehle_worte("Python ist cool"))  # 3
