# 4.4: Sets

# Sets sind container. Sets sind unordered und immutable. Sprich, man kann sie nicht 
# verändern und man kann die Werte nicht mit dem index abrufen. Da man die Werte nicht
# mit dem index abrufen kann, muss jeder Wert einzigartig sein.
# Sets erkennt man an folgender Syntax:

set_name = {"ein Wert", 2, True}
print("Unser set: ", set_name)
# Zuerst definiert man einen Namen. Darauf folgt der assignment operator =. Das set wird
# dann mit { geöffnet. Man kann dann beliebig viele Werte, mit beliebigen Datentypen 
# eintragen. Jeder Wert muss durch ein Komma getrennt sein. Abgeschlossen wird das set mit }.

# Um die Werte in einem set abzurufen, verwendet man die membership operators "in" oder "not in".
# Hier ein paar Beispiele:
print()
print("Alle Werte im set: ")
for x in set_name:
  print(x)
  
print()
print("Prüfen, ob ein Wert im set ist: ")
print("ein Wert" in set_name)

print()
print("Prüfen, ob ein Wert nicht im set ist: ")
print("ein Wert" not in set_name)


# Obwohl ein set immutable ist, kann man trotzdem Werte hinzufügen oder entfernen. Dafür gibt es 
# die folgenden functions:

# - set.add(x)
# - set.remove(x)

# TODO:
# 1. Erstelle ein set mit 5 Werten.
# 2. Loope über jeden Wert in dem set und gib ihn mit print() aus.
# 3. Füge dem set einen Wert hinzu und entferne einen anderen Wert. Gib das Ergebnis mit print() 
# aus.