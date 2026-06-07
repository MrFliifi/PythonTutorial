# 4.2: Lists

# lists sind container. Es ist also eine Variable, die 0 bis n Werte beinhalten kann.
# lists sind ordered und mutable.
# lists erkennt man an folgendem Syntax:

list_name = ["ein Wert", 2, True]
print("Unsere list: ", list_name)
print()

# Zuerst definiert man einen Namen. Darauf folgt der assignment operator =. Die list wird
# dann mit [ geöffnet. Man kann dann beliebig viele Werte, mit beliebigen Datentypen 
# eintragen. Jeder Wert muss durch ein , getrennt sein. Abschließen tut man die list mit ].

# Da lists ordered sind, kann man die Werte der list mit dem Index abrufen.
print("Das sind die Werte der list: ")
print(list_name[0])
print(list_name[1])
print(list_name[2])

# Da lists mutable sind, kann man die Werte der list verändern. Dafür gibt es mehrere functions:
# list.append(x) # Hängt x ans Ende der list
# list.remove(x) # Entfernt den ersten Wert x aus der list
# list.sort()    # Sortiert die list alphabetisch / numerisch

# Man kann den Wert einer list auch mit dem index verändern.
# list[i] = x    # Damit wird der Wert am index i mit dem Wert von x überschrieben.


# TODO:
# 1. Erstelle eine list mit 5 Werten und gib sie mit print() in die Konsole aus.
# 2. appende drei weitere Werte an die list und gib sie mit print() in die Konsole aus.
# 3. remove zwei Werte aus der list und gib sie mit print() in die Konsole aus.
# 4. Überschreibe den dritten Wert der list und gib sie mit print() in die Konsole aus.
# 5. sort die list und gib sie mit print() in die Konsole aus.