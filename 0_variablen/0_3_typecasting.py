# 0.3: Typecasting

# Man kann den Datentyp einer Variablen in Python mit sogenannten "typecasting" oder "type 
# conversion" ändern. Das ist möglich, weil Python dynamisch typisiert ist, was bedeutet, 
# dass der Datentyp einer Variable zur Laufzeit bestimmt wird und sich ändern kann. Es gibt 
# eingebaute Funktionen, die es ermöglichen, Werte von einem Datentyp in einen anderen zu 
# konvertieren. Hier sind einige der häufigsten Funktionen für das typecasting:

# int(): Konvertiert einen Wert in einen integer (Ganzzahl).
# float(): Konvertiert einen Wert in einen float (Gleitkommazahl).
# str(): Konvertiert einen Wert in einen string (Text).
# bool(): Konvertiert einen Wert in einen boolean (True oder False).

# Beispiel: Konvertieren eines strings in einen integer
zahl_string = "42"
print("zahl_string:", zahl_string)  # Ausgabe: "42"

zahl_integer = int(zahl_string)  # Konvertiert den String "42" in die Ganzzahl 42
print("zahl_integer:", zahl_integer)  # Ausgabe: 42

# Nicht jeder Wert kann in einen anderen Typ konvertiert werden. Zum Beispiel kann der string 
# "Hallo" nicht in einen integer oder einen float konvertiert werden, da er keine gültige Zahl 
# darstellt. In solchen Fällen wird eine Fehlermeldung ausgegeben.


# TODO:
# 1. Definiere eine Variable mit einem String-Wert, der eine Zahl repräsentiert (z.B. "3.14"). 
# Konvertiere diesen String in einen Float und gebe das Ergebnis mit print() aus.
# 2. Definiere eine Variable mit einem string-Wert, der kein gültiger integer oder float ist 
# (z.B. "Hallo"). Versuche, diesen string in einen integer oder float zu konvertieren und beobachte, 
# was passiert.
# 3. Definiere eine Variable mit einem integer-Wert. Konvertiere diesen integer in einen string 
# und gebe das Ergebnis mit print() aus.
# 4. Definiere eine Variable mit einem float-Wert. Konvertiere diesen float in einen integer und 
# gebe das Ergebnis mit print() aus. Was fällt dir auf?
# 5. Definiere eine Variable mit einem integer-Wert. Konvertiere diesen integer in einen float 
# und gebe das Ergebnis mit print() aus. Was fällt dir auf?
# 6. Definiere eine Variable mit einem string-Wert, der "True" oder "False" repräsentiert. 
# Konvertiere diesen string in einen boolean und gebe das Ergebnis mit print() aus.
# 7. Definiere eine Variable mit einem integer-Wert. Konvertiere diesen integer in einen boolean 
# und gebe das Ergebnis mit print() aus.