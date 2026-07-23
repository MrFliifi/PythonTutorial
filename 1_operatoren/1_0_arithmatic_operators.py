# 1.0.0: Arithmatic operators

# Arithmatische Operatoren kennen wir bereits aus der Mathematik. Sie ermöglichen es uns, 
# mathematische Operationen durchzuführen. In Python gibt es die folgenden arithmatischen 
# Operatoren:
# +   | Addition
# -   | Subtraktion
# *   | Multiplikation
# /   | Division
# //  | Ganzzahlige Division
# %   | Modulo (Rest der Division)
# **  | Exponentiation (Potenzierung)

# Die ersten vier werde ich nicht weiter erklären. Sie funktionieren genau wie in der Mathematik.

# Die ganzzahlige Division (//) gibt den ganzzahligen Anteil der Division zurück. Zum Beispiel:
print("10 // 3: ", 10 // 3)   # Ausgabe: 3. Der Rest wird also fallen gelassen.

# Der Modulo-Operator (%) gibt den Rest der Division zurück. Zum Beispiel:
print("10 % 3: ", 10 % 3)     # Ausgabe: 1. Hierbei wird nur der Rest zurückgegeben.

# Der Exponentiations-Operator (**) gibt die Potenz einer Zahl zurück. Zum Beispiel:
print("2 ** 3: ", 2 ** 3)     # Ausgabe: 8. 2 hoch 3 ergibt 8.  

# Wenn du mit dem Ergebnis der arithmatischen Operationen weiterrechnen möchtest, musst 
# du die Ergebnisse in Variablen speichern. Zum Beispiel: 
ergebnis = 10 + 5
print("Ergebnis: ", ergebnis)  # Ausgabe: 15

# Du kannst auch mit dem Namen der Variablen weiterrechnen. Zum Beispiel:
ergebnis = ergebnis * 2
print("Ergebnis: ", ergebnis)  # Ausgabe: 30

# TODO:
# 1. Definiere zwei Variablen mit integer-Werten.
# 2. Definiere zwei Variablen mit float-Werten.
# 3. Führe alle arithmatischen Operationen mit diesen Variablen durch und gib die Ergebnisse 
# mit print() aus.
# 4. Definiere eine Variable mit einem string-Wert. Versuche alle arithmatischen Operationen 
# mit dieser Variable durchzuführen und beobachte, welche Ergebnisse du erhältst. Verwende dafür 
# die Variable mit dem string-Wert und eine der Variablen mit den integer- oder float-Werten. Gib
# die Ergebnisse mit print() aus. Was fällt dir auf? Welche Operationen funktionieren und welche 
# nicht?