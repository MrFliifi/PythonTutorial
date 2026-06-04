# 0.3: typercasting

# Man kann den Datentyp einer Variable in Python mit sogenannten "typecasting" oder "type conversion" ändern. 
# Das ist möglich, weil Python dynamisch typisiert ist, was bedeutet, dass der Datentyp einer Variable zur Laufzeit 
# bestimmt wird und sich ändern kann. Es gibt eingebaute Funktionen, die es ermöglichen, Werte von einem Datentyp in 
# einen anderen zu konvertieren. 
# Hier sind einige der häufigsten Funktionen für die Typumwandlung:

# int(): Konvertiert einen Wert in einen Integer (Ganzzahl).
# float(): Konvertiert einen Wert in einen Float (Gleitkommazahl).
# str(): Konvertiert einen Wert in einen String (Text).
# bool(): Konvertiert einen Wert in einen Boolean (True oder False).

# Beispiel: Konvertieren eines Strings in einen Integer
zahl_string = "42"
print("zahl_string:", zahl_string)  # Ausgabe: "42"

zahl_integer = int(zahl_string)  # Konvertiert den String "42" in die Ganzzahl 42
print("zahl_integer:", zahl_integer)  # Ausgabe: 42

# nicht jeder Wert kann in einen anderen Typ konvertiert werden. Zum Beispiel kann der String "Hallo" nicht in 
# einen Integer oder einen Float konvertiert werden, da er keine gültige Zahl darstellt. In solchen Fällen wird 
# eine Fehlermeldung ausgegeben.


# TODO:
# 1. Definiere eine Variable mit einem String-Wert, der eine Zahl repräsentiert (z.B. "3.14"). Konvertiere diesen 
# String in einen Float und gebe das Ergebnis mit print() aus.
# 2. Definiere eine Variable mit einem String-Wert, der kein gültiger Integer oder Float ist (z.B. "Hallo"). Versuche, diesen String in 
# einen Integer oder Float zu konvertieren und beobachte, was passiert.
# 3. Definiere eine Variable mit einem Integer-Wert. Konvertiere diesen Integer in einen String und gebe das Ergebnis mit print() aus.
# 4. Definiere eine Variable mit einem Float-Wert. Konvertiere diesen Float in einen Integer und gebe das Ergebnis mit print() aus. 
# Was fällt dir auf?
# 5. Definiere eine Variable mit einem Integer-Wert. Konvertiere diesen Integer in einen Float und gebe das Ergebnis mit print() aus. 
# Was fällt dir auf?
# 6. Definiere eine Variable mit einem String-Wert, der "True" oder "False" repräsentiert. Konvertiere diesen String in einen Boolean 
# und gebe das Ergebnis mit print() aus.
# 7. Definiere eine Variable mit einem Integer-Wert. Konvertiere diesen Integer in einen Boolean und gebe das Ergebnis mit print() aus.