# 1.2: Comparison operators

# Comparison operators ermöglichen es uns, Werte miteinander zu vergleichen. 
# Sie geben immer einen Boolean-Wert (True oder False) zurück. Es gibt die 
# folgenden comparison operators in Python:

# ==  | Gleichheit
# !=  | Ungleichheit
# >   | Größer als
# <   | Kleiner als
# >=  | Größer oder gleich
# <=  | Kleiner oder gleich

# == vergleicht, ob zwei Werte gleich sind. Zum Beispiel:
print("5 == 5: ", 5 == 5)     # Ausgabe: True
print("5 == 10: ", 5 == 10)   # Ausgabe: False

# != vergleicht, ob zwei Werte ungleich sind. Zum Beispiel:
print("5 != 5: ", 5 != 5)     # Ausgabe: False 
print("5 != 10: ", 5 != 10)   # Ausgabe: True

# > vergleicht, ob der linke Wert größer als der rechte Wert ist. Zum Beispiel:
print("5 > 3: ", 5 > 3)       # Ausgabe: True
print("5 > 10: ", 5 > 10)     # Ausgabe: False

# < vergleicht, ob der linke Wert kleiner als der rechte Wert ist. Zum Beispiel:
print("5 < 10: ", 5 < 10)     # Ausgabe: True
print("5 < 3: ", 5 < 3)       # Ausgabe: False

# >= vergleicht, ob der linke Wert größer oder gleich dem rechten Wert ist. Zum Beispiel:
print("5 >= 5: ", 5 >= 5)     # Ausgabe: True
print("5 >= 3: ", 5 >= 3)     # Ausgabe: True
print("5 >= 10: ", 5 >= 10)   # Ausgabe: False

# <= vergleicht, ob der linke Wert kleiner oder gleich dem rechten Wert ist. Zum Beispiel:
print("5 <= 5: ", 5 <= 5)     # Ausgabe: True
print("5 <= 10: ", 5 <= 10)   # Ausgabe: True
print("5 <= 3: ", 5 <= 3)     # Ausgabe: False


# comparison operators können auch mit Variablen verwendet werden. Zum Beispiel:
a = 5   
b = 10
print("a == b: ", a == b)     # Ausgabe: False
print("a != b: ", a != b)     # Ausgabe: True
print("a > b: ", a > b)       # Ausgabe: False

# Comparison operators sind nützlich, um Bedingungen zu überprüfen und Entscheidungen 
# in unserem Code zu treffen. Dazu mehr im Kapitel über Kontrollflüsse.

# TODO:
# 1. Definiere vier Variablen mit unterschiedlichen Datentypen (integer, float, string, boolean).
# 2. Vergleiche diese Variablen miteinander mit allen comparison operators und gib die Ergebnisse 
# mit print() aus. Beobachte, welche Vergleiche möglich sind und welche nicht. Was fällt dir auf? 
# Welche Datentypen können miteinander verglichen werden und welche nicht?